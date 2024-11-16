from ninja_extra.testing import TestClient
from ninja_jwt.controller import NinjaJWTDefaultController

from user.models import CustomUser


def get_auth_header(user: CustomUser) -> dict[str, str]:
    client = TestClient(NinjaJWTDefaultController)
    data = {
        "username": user.username,
        "password": "1234"
    }
    response = client.post("/pair", json=data, content_type="json")
    return {"Authorization": f'Bearer {response.json()["access"]}'}
