from datetime import datetime, timedelta
from ninja import Schema
from pydantic import PositiveInt
from django.utils.timezone import now
from product.schemas import ProductOutForCart


class BaseCartItem(Schema):
    count: PositiveInt
    delivery_date: datetime = now() + timedelta(7)


class CartItem(BaseCartItem):
    product: ProductOutForCart


class AddCartItem(BaseCartItem):
    product_id: int


class CartItemOut(CartItem):
    id: int
