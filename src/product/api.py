import json
import logging
from django.db import connection
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, PatchDict, UploadedFile
from ninja_extra import ControllerBase, api_controller, route, permissions
from ninja_extra.permissions.common import IsAdminUser

from category.models import CategoryHasProduct
from product.models import Product
from product.permissions import IsOwnerProduct, IsSeller
from product.schemas import CreateProduct, PatchProduct, ProductOut
from services.media_writer import UploadMediaFile

logger = logging.getLogger("cons")

@api_controller(tags=["products"], )
class ProductAPI(ControllerBase):
    @route.post("/", response={201: ProductOut}, permissions=[IsSeller])
    def create_product(self, product: CreateProduct, file: File[UploadedFile]):
        request: HttpRequest = self.context.request #type: ignore
        data = {
            "name": product.name,
            "price": product.price,
            "count": product.count,
            "about": json.dumps(product.about),
            "img": "/",
            "seller_id": request.user.pk
        }
        data = list(data.values())
        template = ', '.join(["%s"] * len(data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_product({template})", data)

        obj = Product.objects.filter(name=product.name).order_by("-id")[0]
        for cat_id in product.category_ids:
            CategoryHasProduct.objects.create(product_id=obj.pk, category_id=cat_id)
        UploadMediaFile(file).write_product_img(obj)
        return obj


    @route.delete(
        "/{product_id}",
        response={204: None},
        permissions=[IsOwnerProduct | IsAdminUser]
    )
    def del_product(self, product_id: int):
        product = get_object_or_404(Product, id=product_id)
        product.delete()


    @route.get("/{product_id}", response={200: ProductOut})
    def get_product(self, product_id: int):
        product = get_object_or_404(Product, id=product_id)
        return product


    @route.get("/", response={200: list[ProductOut]})
    def list_products(self):
        products = Product.objects.all()
        return products


    @route.patch(
        "/{product_id}",
        response={200: ProductOut},
        permissions=[IsOwnerProduct | IsAdminUser]
    )
    def patch_product(self,
        product_id: int,
        payload: PatchDict[PatchProduct],
        file: UploadedFile = File(None)
    ):
        obj = get_object_or_404(Product, id=product_id)
        if payload.get("about"):
            obj.about = obj.about | payload.pop("about")
        if file:
            UploadMediaFile(file).write_product_img(obj)

        for attr, val in payload.items():
            setattr(obj, attr, val)
        obj.save()
        return obj
