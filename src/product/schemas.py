from typing import Any
from ninja import Schema
from ninja.schema import Field
from pydantic import PositiveInt

from user.schemas import Profile


class Product(Schema):
    name: str = Field(max_length=255)
    price: PositiveInt
    count: PositiveInt


class CreateProduct(Product):
    about: dict[str, Any] | None = None


class PatchProduct(Product):
    pass


class ProductOut(Product):
    id: int
    seller: Profile
    img: str
    about: dict[str, Any] | None = None
