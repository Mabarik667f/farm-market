import logging
import pytest
import json
from ninja import UploadedFile
from ninja_extra.testing import TestClient
from product.api import ProductAPI
from product.models import Product
from tests.helpers.api import create_category
from user.models import CustomUser
from category.models import Category, CategoryHasProduct
from tests.helpers import create_img, BaseTestClass, ProductData

logger = logging.getLogger("cons")


@pytest.fixture
def p_client():
    return TestClient(ProductAPI)


@pytest.fixture
def create_new_category():
    return create_category("Specially")


class TestCasesforProducts(BaseTestClass):

    img = UploadedFile(file=create_img())

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
        assert j["img"] == f"/media/product{j["id"]}/dummy.png"
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

    def tests_get_product(self, p_client: TestClient, new_product: ProductData):
        response = p_client.get(f'/{new_product.product.pk}')
        assert response.status_code == 200
        assert response.json()["name"]

    def tests_get_list_products(self, p_client: TestClient, new_product: ProductData):
        response = p_client.get(f'/')
        assert response.status_code == 200
        assert len(response.json()["items"]) == 1

    def tests_del_product(
        self,
        p_client: TestClient,
        new_product: ProductData,
        new_user: CustomUser
    ):
        self.set_headers(new_product.user)
        response = p_client.delete(f'/{new_product.product.pk}', headers=self.headers, user=new_user)
        assert response.status_code == 403

        response = p_client.delete(f'/{new_product.product.pk}', headers=self.headers, user=new_product.user)
        assert response.status_code == 204

    def tests_patch_product(
        self,
        p_client: TestClient,
        new_product: ProductData
    ):
        self.set_headers(new_product.user)
        self.headers["Content-Type"] = "multipart/form-data"
        new_data = {"payload": json.dumps({
            "count": 100,
            "about": {
                "mass": 200,
                "t": "ls"
            }
        })}

        response = p_client.patch(f"/{new_product.product.pk}", headers=self.headers,
            data=new_data, FILES={"file": self.img}, user=new_product.user)

        j = response.json()
        assert response.status_code == 200
        assert j["count"] == 100
        assert j["about"]['mass'] == 200 and j["about"]["t"] == "ls"
        assert j["img"] == f"/media/product{new_product.product.pk}/dummy.png"

    def tests_add_category_for_product(
        self,
        p_client: TestClient,
        new_product: ProductData,
        create_new_category: Category
    ):
        self.set_headers(new_product.user)
        response = p_client.put(f"/{new_product.product.pk}/{create_new_category.pk}",
            headers=self.headers)

        assert response.status_code == 201
        assert len(response.json()["categories"]) == 3

    def tests_del_category_for_product(
        self,
        p_client: TestClient,
        new_product: ProductData
    ):
        self.set_headers(new_product.user)
        pr_id = new_product.product.pk
        categories = CategoryHasProduct.objects.filter(product_id=pr_id).prefetch_related("category")
        response = p_client.delete(f"/{pr_id}/{categories[0].category.pk}",
            headers=self.headers)

        assert response.status_code == 200
        assert len(response.json()["categories"]) == 1

        response = p_client.delete(f"/{pr_id}/{categories[0].category.pk}",
            headers=self.headers)

        assert response.status_code == 400
        assert CategoryHasProduct.objects.count() == 1
