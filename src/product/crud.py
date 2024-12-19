import json
import logging

from datetime import datetime
from django.db import IntegrityError, connection
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from ninja import File, PatchDict, UploadedFile

from category.models import CategoryHasProduct
from product.models import Product
from product.exceptions import OneCategoryRequiredForProductError
from product.schemas import CreateProduct, PatchProduct
from services.media_writer import UploadMediaFile

logger = logging.getLogger("cons")


def create_product(
    user_id: int, product: CreateProduct, file: File[UploadedFile]
) -> Product:
    data = {
        "name": product.name,
        "price": product.price,
        "count": product.count,
        "mass": product.mass,
        "shelf_life": product.shelf_life,
        "about": json.dumps(product.about),
        "img": file.name,
        "seller_id": user_id,
    }
    data = list(data.values())
    template = ", ".join(["%s"] * len(data))
    with connection.cursor() as cursor:
        cursor.execute(f"CALL create_product({template})", data)

    obj = Product.objects.filter(name=product.name).order_by("-id")[0]
    for cat_id in product.category_ids:
        CategoryHasProduct.objects.create(product_id=obj.pk, category_id=cat_id)
    UploadMediaFile(file).write_product_img(obj)
    return obj


def del_product(product_id: int) -> None:
    get_product(product_id).delete()


def get_product(product_id: int) -> Product:
    return get_object_or_404(Product, id=product_id)


def list_products(category_ids: list[int] = []) -> list[Product]:
    if category_ids:
        q = CategoryHasProduct.objects.filter(category_id__in=category_ids).distinct(
            "product_id"
        )
    else:
        q = CategoryHasProduct.objects.all().distinct("product_id")
    q.select_related("product")
    return [obj.product for obj in q]


def add_category_for_product(product_id: int, cat_id: int) -> Product:
    pr = get_product(product_id)
    try:
        CategoryHasProduct.objects.get_or_create(
            product_id=product_id, category_id=cat_id
        )
        return pr
    except IntegrityError:
        raise Http404("Категории не существует!")


def del_category_for_product(product_id: int, cat_id: int) -> Product:
    pr = get_product(product_id)
    if len(get_list_or_404(CategoryHasProduct, product_id=product_id)) <= 1:
        raise OneCategoryRequiredForProductError()

    cat_has_pr = get_object_or_404(
        CategoryHasProduct, category_id=cat_id, product_id=product_id
    )
    cat_has_pr.delete()
    return pr


def patch_product(
    product_id: int,
    payload: PatchDict[PatchProduct],
) -> Product:
    obj = get_product(product_id)
    if payload.get("about"):
        obj.about = obj.about | payload.pop("about")
    if payload.get("shelf_life"):
        payload["shelf_life"] = datetime.strftime(
            payload.get("shelf_life", datetime.now()), "%Y-%m-%d"
        )
    for attr, val in payload.items():
        setattr(obj, attr, val)
    obj.save()
    return obj


def update_img_product(product_id: int, file: UploadedFile) -> Product:
    obj = get_product(product_id)
    UploadMediaFile(file).write_product_img(obj)
    return obj
