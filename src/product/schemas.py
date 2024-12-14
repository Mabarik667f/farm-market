from datetime import date
import logging
from typing import Any
from ninja import Schema
from ninja.schema import Field
from pydantic import PositiveInt

from user.schemas import Profile
from category.schemas import Category

logger = logging.getLogger("cons")

class Product(Schema):
    name: str = Field(max_length=255)
    price: PositiveInt
    count: PositiveInt
    mass: float
    shelf_life: date


class CreateProduct(Product):
    about: dict[str, Any] | None = None
    category_ids: list[int]


class PatchProduct(Schema):
    name: str | None = None
    price: PositiveInt | None = None
    count: PositiveInt | None = None
    about: dict[str, Any] | None = None
    mass: float | None = None
    shelf_life: date | None = None

class ProductOut(Product):
    id: int
    seller: Profile
    img: str
    about: dict[str, Any] | None = None
    categories: list[Category]


class ProductOutForOrder(Schema):
    id: int
    name: str
    price: PositiveInt
    mass: float
    seller: Profile
    img: str
