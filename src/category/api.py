from django.db import connection
from django.shortcuts import get_object_or_404
from ninja_extra import ControllerBase, api_controller, permissions, route

from category.schemas import CategoryOut, CreateCategory
from category.models import Category as CategoryModel

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
        obj = CategoryModel.objects.get(id=category_id)
        obj.delete()
