from django.db import connection
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from category.schemas import CategoryOut, CreateCategory
from category.models import Category as CategoryModel
router = Router(tags=["categories"])


@router.post('/', response={201: CategoryOut})
def create_category(request: HttpRequest, payload: CreateCategory):
    template = ", ".join(['%s'])
    with connection.cursor() as cursor:
        cursor.execute(f"CALL create_category({template})", [payload.name])
    obj = CategoryModel.objects.filter().order_by("-id")[0]
    return obj


@router.get('/{category_id}', response={200: CategoryOut})
def get_category(request: HttpRequest, category_id: int):
    obj = get_object_or_404(CategoryModel, id=category_id)
    return obj


@router.get("/", response={200: list[CategoryOut]})
def list_categories(request):
    qs = CategoryModel.objects.all()
    return qs


@router.delete("/{category_id}", response={204: None})
def del_category(request: HttpRequest, category_id: int):
    obj = CategoryModel.objects.get(id=category_id)
    obj.delete()
