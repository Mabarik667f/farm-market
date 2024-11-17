import logging
import pytest
import json
from ninja import UploadedFile
from ninja_extra.testing import TestClient
from product.api import ProductAPI
from product.models import Product
from user.models import CustomUser
from category.models import Category
from tests.helpers import create_img, get_auth_header

logger = logging.getLogger("cons")


@pytest.fixture
def p_client():
    return TestClient(ProductAPI)


class TestCasesforProducts:

    img = UploadedFile(file=create_img())

    def set_headers(self, user: CustomUser) -> None:
        self.headers = dict() | get_auth_header(user)

    def get_product_data(self, categories: list[Category]):
        product_data = {
            "product":
                json.dumps(
                {
                    "name": "string",
                    "price": 1,
                    "count": 1,
                    "about": {
                        "mass": 100
                    },
                    "category_ids": [cat.pk for cat in categories]
                }
            )
        }
        return product_data

    def tests_create_product(
        self,
        p_client: TestClient,
        create_seller: CustomUser,
        list_categories: list[Category]
    ):
        self.set_headers(create_seller)
        self.headers["Content-Type"] = "multipart/form-data"

        response = p_client.post('/', data=self.get_product_data(list_categories),
            FILES={"file": self.img}, headers=self.headers, user=create_seller)

        j = response.json()
        assert response.status_code == 201
        assert j["img"] == "/media/product1/dummy.png"
        assert len(j["about"]) == 1
        assert len(j["categories"]) == 2

    def tests_fail_create_product(
        self,
        p_client: TestClient,
        new_user: CustomUser,
        list_categories: list[Category]
    ):
        self.set_headers(new_user)
        self.headers["Content-Type"] = "multipart/form-data"

        response = p_client.post('/', data=self.get_product_data(list_categories),
            FILES={"file": self.img}, headers=self.headers, user=new_user)

        assert response.status_code == 403

    def tests_get_product(self, p_client: TestClient, new_product: tuple[Product, CustomUser]):
        response = p_client.get(f'/{new_product[0].pk}')
        assert response.status_code == 200
        assert response.json()["name"]

    def tests_get_list_products(self, p_client: TestClient, new_product: tuple[Product, CustomUser]):
        response = p_client.get(f'/')
        assert response.status_code == 200
        assert len(response.json()) == 1

    def tests_del_product(
        self,
        p_client: TestClient,
        new_product: tuple[Product, CustomUser],
        new_user: CustomUser
    ):
        self.set_headers(new_product[1])
        response = p_client.delete(f'/{new_product[0].pk}', headers=self.headers, user=new_user)
        assert response.status_code == 403

        response = p_client.delete(f'/{new_product[0].pk}', headers=self.headers, user=new_product[1])
        assert response.status_code == 204

    def tests_patch_product(
        self,
        p_client: TestClient,
        new_product: tuple[Product, CustomUser]
    ):
        self.set_headers(new_product[1])
        self.headers["Content-Type"] = "multipart/form-data"
        new_data = {"payload": json.dumps({
            "count": 100,
            "about": {
                "mass": 200,
                "t": "ls"
            }
        })}

        response = p_client.patch(f"/{new_product[0].pk}", headers=self.headers,
            data=new_data, FILES={"file": self.img}, user=new_product[1])

        j = response.json()
        assert response.status_code == 200
        assert j["count"] == 100
        assert j["about"]['mass'] == 200 and j["about"]["t"] == "ls"
        assert j["img"] == f"/media/product{new_product[0].pk}/dummy.png"
