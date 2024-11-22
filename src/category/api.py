from django.db import connection
from django.shortcuts import get_object_or_404
from ninja_extra import ControllerBase, api_controller, route

from product.exceptions import OneCategoryRequiredForProductError
from category.schemas import CategoryOut, CreateCategory
from category.models import Category as CategoryModel, CategoryHasProduct

@api_controller("/categories", tags=["categories"], permissions=[])
class CategoryAPI(ControllerBase):
    @route.post('/', response={201: CategoryOut})
    def create_category(self, payload: CreateCategory):
        template = ", ".join(['%s'])
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_category({template})", [payload.name])
        obj = CategoryModel.objects.filter().order_by("-id")[0]
        return obj

    @route.get('/{category_id}', response={200: CategoryOut})
    def get_category(self, category_id: int):
        obj = get_object_or_404(CategoryModel, id=category_id)
        return obj

    @route.get("/", response={200: list[CategoryOut]})
    def list_categories(self):
        qs = CategoryModel.objects.all()
        return qs

    @route.delete("/{category_id}", response={204: None})
    def del_category(self, category_id: int):
        obj = get_object_or_404(CategoryModel, id=category_id)
        cats_has_prs = CategoryHasProduct.objects.filter(category_id=category_id).prefetch_related("product")
        for cat_has_pr in cats_has_prs:
            if CategoryHasProduct.objects.filter(product_id=cat_has_pr.product.pk).count() <= 1:
                raise OneCategoryRequiredForProductError
        obj.delete()
