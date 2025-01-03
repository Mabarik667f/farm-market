from datetime import date
import logging
from typing import Any
from ninja import Schema
from ninja.schema import Field
from pydantic import PositiveInt

from category.models import CategoryHasProduct
from user.schemas import Profile, SellerOutForProduct
from category.schemas import CategoryOut
from user.models import CustomUser
from product.models import Product as ProductModel

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
    categories: list[CategoryOut]

class SingleProductOut(Product):
    id: int
    seller: SellerOutForProduct
    img: str
    about: dict[str, Any] | None = None
    categories: list[CategoryOut]



class ProductOutForCart(Product):
    id: int
    img: str
    seller: Profile


class ProductOutForList(Product):
    id: int
    img: str
    seller: SellerOutForProduct


class ProductOutForOrder(Schema):
    id: int
    name: str
    price: PositiveInt
    mass: float
    seller: Profile
    img: str


def get_seller_out_for_product_schema(product: ProductModel) -> ProductOutForList:
    return ProductOutForList(
        id=product.pk,
        name=product.name,
        count=product.count,
        price=product.price,
        shelf_life=product.shelf_life,
        mass=product.mass,
        img=product.img,
        seller=SellerOutForProduct(
            username=CustomUser.objects.get(pk=product.seller.pk).username
        ),
    )


def get_seller_out_for_single_product_schema(product: ProductModel) -> SingleProductOut:
    category_ids = CategoryHasProduct.objects.filter(product_id=product.pk).select_related("category")
    categories = [CategoryOut(id=c.category.pk, name=c.category.name) for c in category_ids]
    return SingleProductOut(id=product.pk,
        name=product.name,
        count=product.count,
        price=product.price,
        shelf_life=product.shelf_life,
        mass=product.mass,
        img=product.img,
        about=product.about,
        categories=categories,
        seller=SellerOutForProduct(username=CustomUser.objects.get(pk=product.seller.pk).username)
    )
