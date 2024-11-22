import logging
import pytest
from ninja_extra.testing import TestClient
from cart.api import CartAPI
from django.utils import timezone

from cart.models import CartItem
from tests.helpers import BaseTestClass, ProductData, CartData
from user.models import CustomUser

logger = logging.getLogger("cons")

@pytest.fixture
def c_client():
    return TestClient(CartAPI)


class TestCasesforCart(BaseTestClass):

    def tests_create_cart_item(
        self,
        c_client: TestClient,
        new_user: CustomUser,
        new_product: ProductData
    ):
        data = {
            "product_id": new_product.product.pk,
            "count": 3,
            "delivery_date": timezone.now()
        }
        response = c_client.post("/", json=data, headers=self.headers)

        assert response.status_code == 401

        self.set_headers(new_user)
        response = c_client.post("/", json=data, headers=self.headers)
        assert response.status_code == 400

        data["count"] = 2
        response = c_client.post("/", json=data, headers=self.headers)

        assert response.status_code == 201
        assert response.json()["product"]["name"] == "string"

    def tests_get_cart(
        self,
        c_client: TestClient,
        new_cart: CartData
    ):
        self.set_headers(new_cart.user)
        response = c_client.get('/', headers=self.headers)

        assert response.status_code == 200
        assert len(response.json()) == 2

    def tests_del_cart_item(
        self,
        c_client: TestClient,
        new_cart: CartData
    ):
        self.set_headers(new_cart.user)
        response = c_client.delete(f"/{new_cart.cart_items[0].pk}", headers=self.headers)

        assert response.status_code == 204
        assert len(CartItem.objects.all()) == 1
