import json
import logging
import shutil
from pathlib import Path
from ninja_extra.testing import TestClient
from ninja_jwt.controller import NinjaJWTDefaultController
import pytest
import os
from django.db import connection
from category.models import Category, CategoryHasProduct
from product.models import Product
from user.models import CustomUser, Role, RoleForUser

from PIL import Image
from io import BytesIO

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
    user = CustomUser.objects.create_user(
        username="testseller",
        email="testuser@example.com",
        password="1234"
    )
    role = Role.objects.get(name="S")
    RoleForUser.objects.create(user_id=user.pk, role_id=role.pk)
    return user


@pytest.fixture(scope="function")
def new_user() -> CustomUser:
    user_data = CustomUser.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="1234"
    )
    return user_data


@pytest.fixture(scope="function")
def list_categories() -> list[Category]:
    cats_data = [
        {"name": "Овощи"},
        {"name": "Фрукты"}
    ]
    resp = []
    for cat in cats_data:
        resp.append(Category.objects.create(name=cat["name"]))
    return resp


@pytest.fixture(scope="function")
def new_product(create_seller: CustomUser, list_categories: list[Category]) -> tuple[Product, CustomUser]:
    pr = Product.objects.create(
        name="string",
        price=1,
        count=1,
        about={"mass": 100},
        img="/",
        seller_id=create_seller.pk
    )
    for cat in list_categories:
        CategoryHasProduct.objects.create(product_id=pr.pk, category_id=cat.pk)
    return (pr, create_seller)


@pytest.fixture(autouse=True)
def monkeypatch_dir(monkeypatch: pytest.MonkeyPatch):
    test_dir = Path("test_dir/")
    test_dir.mkdir(exist_ok=True)
    monkeypatch.chdir("test_dir/")
    os.mkdir("media")
    yield
    monkeypatch.chdir("..")
    shutil.rmtree("test_dir/")
