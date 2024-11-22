import json
import logging
import shutil
import pytest
import os

from pathlib import Path
from django.db import connection
from cart.models import CartItem
from category.models import Category
from tests.helpers.common import OrderData
from user.models import CustomUser, Role, RoleForUser
from tests.helpers import ProductData, CartData
from tests.helpers.api import create_category, create_order, create_product, create_cart_item, create_user

logger = logging.getLogger("cons")


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture(autouse=True)
def execute_sql_files():

    files = ["procedures.sql", "trigger_functions.sql", "triggers.sql", "insert_values.sql"]
    for f in files:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", f"sql_scripts/{f}"))

        with open(path, "r") as f:
            sql_script = f.read()

        with connection.cursor() as cursor:
            cursor.execute(sql_script)


@pytest.fixture(scope="function")
def create_seller():
    user = create_user("testseller", "testuser2@example.com")
    role = Role.objects.get(name="S")
    RoleForUser.objects.create(user_id=user.pk, role_id=role.pk)
    return user


@pytest.fixture(scope="function")
def new_user() -> CustomUser:
    return create_user("testuser", "testuser@example.com")


@pytest.fixture(scope="function")
def list_categories() -> list[Category]:
    cats_data = [
        {"name": "Овощи"},
        {"name": "Фрукты"}
    ]
    resp = []
    for cat in cats_data:
        resp.append(create_category(name=cat["name"]))
    return resp


@pytest.fixture(scope="function")
def new_product(create_seller: CustomUser, list_categories: list[Category]) -> ProductData:
    pr = create_product(create_seller.pk, categories=list_categories)
    return ProductData(pr, create_seller)


@pytest.fixture(scope="function")
def new_cart(
    new_user: CustomUser,
    create_seller: CustomUser,
    list_categories: list[Category]
) -> CartData:
    cart = []
    for _ in range(2):
        pr = create_product(create_seller.pk, categories=list_categories)
        cart.append(create_cart_item(pr.pk, new_user.pk))
    return CartData(new_user, cart)


@pytest.fixture(scope="function")
def new_order(
    new_cart: CartData
) -> OrderData:
    order = create_order(new_cart.user.pk, new_cart.cart_items)
    return OrderData(new_cart.user, order)


@pytest.fixture(autouse=True)
def monkeypatch_dir(monkeypatch: pytest.MonkeyPatch):
    test_dir = Path("test_dir/")
    test_dir.mkdir(exist_ok=True)
    monkeypatch.chdir("test_dir/")
    media = Path("media/")
    media.mkdir(exist_ok=True)
    yield
    monkeypatch.chdir("..")
    shutil.rmtree("test_dir/")
