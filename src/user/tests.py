import logging
import os
from django.urls import reverse
from django.db import connection
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase
from user.models import CustomUser, Profile, RoleForUser

logger = logging.getLogger("cons")

def create_user():
    user = CustomUser.objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="testpass123"
    )
    return user


class UserTestCases(APITestCase):
    client: APIClient

    def setUp(self) -> None:
        self.client = APIClient()
        files = ["procedures.sql", "trigger_functions.sql", "triggers.sql", "insert_values.sql"]
        for f in files:
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", f"sql_scripts/{f}"))

            with open(path, "r") as f:
                sql_script = f.read()

            with connection.cursor() as cursor:
                cursor.execute(sql_script)

    def tests_register_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
            "password2": "testpass123"
        }
        response: Response = self.client.post("/api/v1/users/register/", data=data, format='json') #type: ignore
        self.assertEqual(response.status_code, 201)

        data["password"] = "rerssdsds"
        response: Response = self.client.post("/api/v1/users/register/", data=data, format='json') #type: ignore
        self.assertEqual(response.status_code, 400)

        self.assertEqual(Profile.objects.get(user_id=1).pk, 1)
        self.assertEqual(len(RoleForUser.objects.filter(user_id=1)), 1)
