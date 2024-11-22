import logging
from ninja_extra.testing import TestClient
from category.api import CategoryAPI
import pytest

from category.models import Category, CategoryHasProduct
from tests.helpers.common import ProductData
logger = logging.getLogger("cons")

@pytest.fixture
def n_client():
    return TestClient(CategoryAPI)

@pytest.fixture
def new_category() -> Category:
    obj = Category.objects.create(name="new cat 1")
    return obj

class TestCasesforCategories():

    def tests_create_category(self, n_client: TestClient):
        data = {"name": "test category 1"}
        response = n_client.post("/", json=data, content_type="json")

        assert response.status_code == 201
        assert response.json()["name"] == "test category 1"

    def tests_get_category(self, n_client: TestClient, new_category: Category):
        response = n_client.get(f"/{new_category.pk}", content_type="json")

        assert response.status_code == 200
        assert response.json()["name"] == "new cat 1"

    def tests_get_list_categories(self, n_client: TestClient, new_category: Category):
        n_client.post("/", json={"name": "test category 1"}, content_type="json")
        response = n_client.get("/", content_type="json")

        assert response.status_code == 200
        assert len(response.json()) == 2

    def tests_del_category(
        self,
        n_client: TestClient,
        new_product: ProductData
    ):
        pr_id = new_product.product.pk
        categories = CategoryHasProduct.objects.filter(product_id=pr_id).prefetch_related("category")
        response = n_client.delete(f"/{categories[0].category.pk}", content_type="json")
        assert response.status_code == 204

        response = n_client.delete(f"/{categories[0].category.pk}", content_type="json")
        assert response.status_code == 400
