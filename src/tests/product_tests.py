import logging
import pytest
import json
from ninja import UploadedFile
from ninja_extra.testing import TestClient
from product.api import ProductAPI
from user.models import CustomUser
from tests.helpers import create_img, get_auth_header

logger = logging.getLogger("cons")


@pytest.fixture
def p_client():
    return TestClient(ProductAPI)


@pytest.fixture
def new_product():
    pass

class TestCasesforProducts:

    product_data = {
        "product":
            json.dumps(
            {
                "name": "string",
                "price": 1,
                "count": 1,
                "about": {
                    "mass": 100
                }
            }
        )
    }

    img = UploadedFile(file=create_img())

    def set_headers(self, user: CustomUser) -> None:
        self.headers = dict() | get_auth_header(user)

    def tests_create_product(self, p_client: TestClient, create_seller: CustomUser):
        self.set_headers(create_seller)
        self.headers["Content-Type"] = "multipart/form-data"

        response = p_client.post('/', data=self.product_data,
            FILES={"file": self.img}, headers=self.headers, user=create_seller)

        j = response.json()
        assert response.status_code == 201
        assert j["img"] == "/media/product1/dummy.png"
        assert len(j["about"]) == 1

    def tests_fail_create_product(self, p_client: TestClient, new_user: CustomUser):
        self.set_headers(new_user)
        self.headers["Content-Type"] = "multipart/form-data"

        response = p_client.post('/', data=self.product_data,
            FILES={"file": self.img}, headers=self.headers, user=new_user)

        assert response.status_code == 403

    def tests_get_product(self, p_client: TestClient):
        pass
