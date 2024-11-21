import logging
from django.db.models import Q
import pytest
from ninja_extra.testing import TestClient
from order.api import OrderAPI
from order.models import Order, OrderItem
from tests.helpers import BaseTestClass
from tests.helpers.common import CartData, OrderData
from user.models import CustomUser

logger = logging.getLogger("cons")


@pytest.fixture
def o_client():
    return TestClient(OrderAPI)


class TestCasesForOrders(BaseTestClass):

    def tests_create_order(self, o_client: TestClient, new_cart: CartData):
        self.set_headers(new_cart.user)
        logger.info(new_cart.cart_items)
        data = {
            "address": "Test adr 123",
            "phone": "79430575519",
            "cart_item_ids": [item.pk for item in new_cart.cart_items]
        }
        response = o_client.post("/", json=data, headers=self.headers)
        assert len(response.json()["products"]) == 2
        assert response.status_code == 201

    def tests_get_order(self, o_client: TestClient, new_order: OrderData):
        self.set_headers(new_order.user)
        response = o_client.get(f"/{new_order.order.pk}", headers=self.headers)
        assert len(response.json()["products"]) == 2
        assert response.status_code == 200

    def tests_get_order_by_non_owner(
        self,
        o_client: TestClient,
        new_order: OrderData,
    ):
        user = CustomUser.objects.get(~Q(id=new_order.user.pk))
        self.set_headers(user)
        response = o_client.get(f"/{new_order.order.pk}", headers=self.headers)
        assert response.status_code == 403

    def tests_del_order(self, o_client: TestClient, new_order: OrderData):
        self.set_headers(new_order.user)
        response = o_client.delete(f"/{new_order.order.pk}", headers=self.headers)
        assert response.status_code == 204
        assert len(Order.objects.all()) == 0 and len(OrderItem.objects.all()) == 0

    def tests_get_history(self, o_client: TestClient, new_order: OrderData):
        self.set_headers(new_order.user)
        response = o_client.get(f"/history/all", headers=self.headers)
        assert len(response.json()) == 1
        assert response.status_code == 200
