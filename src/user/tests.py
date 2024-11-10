import logging
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APIClient, APITestCase

from user.models import CustomUser

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

    def tests_register_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
            "password2": "testpass123"
        }
        response: Response = self.client.post("/api/v1/user/register/", data=data, format='json') #type: ignore
        self.assertEqual(response.status_code, 201)

        data["password"] = "rerssdsds"
        response: Response = self.client.post("/api/v1/user/register/", data=data, format='json') #type: ignore
        self.assertEqual(response.status_code, 400)
