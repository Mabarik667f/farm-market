import logging
from ninja_extra import NinjaExtraAPI
from ninja.security import APIKeyHeader
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTBaseAuthentication
from django.http import HttpRequest

from category.api import CategoryAPI
from user.api import UserAPI
from product.api import ProductAPI
from cart.api import router as cart_router
from order.api import router as order_router
from user.models import CustomUser

logger = logging.getLogger("cons")

class GlobalAuth(APIKeyHeader, JWTBaseAuthentication):

    def __init__(self) -> None:
        super().__init__()
        self.user_model = CustomUser

    def authenticate(self, request: HttpRequest, key):
        if not key:
            key = ""
        return self.jwt_authenticate(request, token=key)

api = NinjaExtraAPI(title="Farm market API", auth=GlobalAuth())
api.register_controllers(NinjaJWTDefaultController)

api.register_controllers(UserAPI)
api.register_controllers(CategoryAPI)
api.register_controllers(ProductAPI)
api.add_router("/cart/", cart_router)
api.add_router("/orders/", order_router)
