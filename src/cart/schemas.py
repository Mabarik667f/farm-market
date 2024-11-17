from datetime import datetime
from ninja import Schema
from pydantic import PositiveInt

from product.schemas import ProductOut


class BaseCartItem(Schema):
    count: PositiveInt
    delivery_date: datetime


class CartItem(BaseCartItem):
    product: ProductOut


class AddCartItem(BaseCartItem):
    product_id: int


class CartItemOut(CartItem):
    id: int
