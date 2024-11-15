import logging
from ninja.testing import TestClient
from product.api import router
import pytest


logger = logging.getLogger("cons")


@pytest.fixture
def p_client():
    return TestClient(router)


class TestCasesforProducts:
    pass
