import logging
import pytest
import os
from django.db import connection
from user.models import CustomUser
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
def create_user():
    user = CustomUser.objects.create_user(
        username="testuser",
        email="testuser@example.com",
    )
    user.set_password("Testpass123")
