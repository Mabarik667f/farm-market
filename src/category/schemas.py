import logging
from ninja import Schema
from pydantic import field_validator

from category.exceptions import UniqueCategoryException
from category.models import Category as CategoryModel
from config.exceptions import UniqueException

logger = logging.getLogger("cons")

class Category(Schema):
    name: str


class CreateCategory(Category):


    @field_validator("name")
    def uniqie_category(cls, v):
        try:
            cat = CategoryModel.objects.filter(name=v)
            if cat.exists():
                raise UniqueException
            return v
        except UniqueException:
            raise UniqueCategoryException("Категория уже существует!")



class CategoryOut(Category):
    id: int
