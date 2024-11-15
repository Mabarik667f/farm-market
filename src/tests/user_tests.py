import logging
from ninja.testing import TestClient
from pluggy import Result
from user.api import router
import pytest

from user.models import CustomUser, Profile, RoleForUser

logger = logging.getLogger("cons")

user_data = {
   "username": "aboba",
   "email": "bobaeff@email.com",
   "password": "+Password447"
}

@pytest.fixture
def u_client():
    return TestClient(router)

@pytest.fixture
def new_user() -> CustomUser:
    obj = CustomUser.objects.create(**user_data)
    return obj


class TestCasesforCategories:

    def tests_register(self, u_client: TestClient):
        data = user_data | {"password2": "+Password447"}
        response = u_client.post('/register', json=data, content_type="json")

        assert response.status_code == 201
        assert response.json()["username"] == "aboba" and response.json()["roles"][0]['name'] == 'D'

        response = u_client.post('/register', json=data, content_type="json")
        assert response.status_code == 400

        bad_data = {
            "username": "sdsds",
            "email": "dasdsadad@fmai.com",
            "password": "+Password447",
            "password2": "dasdad"
        }
        response = u_client.post('/register', json=bad_data, content_type="json")
        assert response.status_code == 400

    def tests_get_user(self, u_client: TestClient, new_user: CustomUser):
        response = u_client.get(f"/{new_user.pk}", content_type="json")

        assert response.status_code == 200
        assert response.json()["username"] == "aboba"

        response = u_client.get(f"/{100}", content_type="json")

        assert response.status_code == 404

    def tests_del_user(self, u_client: TestClient, new_user: CustomUser):
        response = u_client.delete(f"/{new_user.pk}", content_type="json")

        assert response.status_code == 204
        assert len(Profile.objects.all()) == 0 and len(RoleForUser.objects.all()) == 0


class TestCasesForRoles:

    def tests_add_role(self, u_client: TestClient, new_user: CustomUser):
        response = u_client.post(f'/role/{new_user.pk}', json={"name": "S"}, content_type="json")

        assert response.status_code == 201
        assert len(response.json()["roles"]) == 2

        response = u_client.post(f'/role/{new_user.pk}', json={"name": "D"}, content_type="json")

        assert response.status_code == 400


    def tests_del_role(self, u_client: TestClient, new_user: CustomUser):
        u_client.post(f'/role/{new_user.pk}', json={"name": "S"}, content_type="json")
        response = u_client.delete(f'/role/{new_user.pk}', json={"name": "S"}, content_type="json")

        assert response.status_code == 204
        assert len(response.json()["roles"]) == 1

        response = u_client.delete(f'/role/{new_user.pk}', json={"name": "D"}, content_type="json")

        assert response.status_code == 400
