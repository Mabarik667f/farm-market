from django.db import connection
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from product.exceptions import OneCategoryRequiredForProductError
from category.schemas import CreateCategory
from category.models import Category as CategoryModel, CategoryHasProduct


def create_category(payload: CreateCategory) -> CategoryModel:
    template = ", ".join(['%s'])
    with connection.cursor() as cursor:
        cursor.execute(f"CALL create_category({template})", [payload.name])
    obj = CategoryModel.objects.filter().order_by("-id")[0]
    return obj


def get_category(category_id: int) -> CategoryModel:
    return get_object_or_404(CategoryModel, id=category_id)


def list_categories() -> QuerySet[CategoryModel]:
    return CategoryModel.objects.all()


def del_category(category_id: int) -> None:
    obj = get_category(category_id)
    cats_has_prs = CategoryHasProduct.objects.filter(category_id=category_id).prefetch_related("product")
    for cat_has_pr in cats_has_prs:
        if CategoryHasProduct.objects.filter(product_id=cat_has_pr.product.pk).count() <= 1:
            raise OneCategoryRequiredForProductError
    obj.delete()
