from dataclasses import dataclass
from cart.models import CartItem
from order.models import Order
from product.models import Product
from user.models import CustomUser
from .headers import get_auth_header

class BaseTestClass:
    headers = {}

    def set_headers(self, user: CustomUser) -> None:
        self.headers = dict() | get_auth_header(user)


@dataclass
class ProductData:
    product: Product
    user: CustomUser


@dataclass
class CartData:
    user: CustomUser
    cart_items: list[CartItem]


@dataclass
class OrderData:
    user: CustomUser
    order: Order
