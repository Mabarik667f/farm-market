import logging
from django.http import HttpRequest
from ninja import File, PatchDict, UploadedFile
from ninja.pagination import paginate
from ninja_extra import ControllerBase, api_controller, route
from ninja_extra.permissions.common import IsAdminUser
from ninja_jwt.authentication import JWTAuth

from product.permissions import IsOwnerProduct, IsSeller
from product.schemas import (
    CreateProduct,
    PatchProduct,
    ProductOut,
    ProductOutForList,
    SingleProductOut,
    get_seller_out_for_single_product_schema,
    get_seller_out_for_product_schema,

)
from product import crud

logger = logging.getLogger("cons")


@api_controller("/products", tags=["products"])
class ProductAPI(ControllerBase):
    @route.post("/", response={201: ProductOut}, permissions=[IsSeller], auth=JWTAuth())
    def create_product(self, product: CreateProduct, file: File[UploadedFile]):
        request: HttpRequest = self.context.request  # type: ignore
        return crud.create_product(request.user.pk, product, file)

    @route.delete(
        "/{product_id}",
        response={204: None},
        permissions=[IsOwnerProduct | IsAdminUser],
        auth=JWTAuth(),
    )
    def del_product(self, product_id: int):
        crud.del_product(product_id)

    @route.get("/list/", response={200: list[ProductOutForList]}, auth=None)
    @paginate
    def list_products(self, category_ids: list[int] = []):
        products = crud.list_products(category_ids)
        return [get_seller_out_for_product_schema(p) for p in products]

    @route.get("/{product_id}", response={200: SingleProductOut}, auth=None)
    def get_product(self, product_id: int):
        product = crud.get_product(product_id)
        return get_seller_out_for_single_product_schema(product)

    @route.put("/{product_id}/{cat_id}", response={201: ProductOut}, auth=JWTAuth())
    def add_category_for_product(self, product_id: int, cat_id: int):
        return crud.add_category_for_product(product_id, cat_id)

    @route.delete("/{product_id}/{cat_id}", response={200: ProductOut}, auth=JWTAuth())
    def del_category_for_product(self, product_id: int, cat_id: int):
        return crud.del_category_for_product(product_id, cat_id)

    @route.post(
        "/{product_id}/img/",
        response={200: ProductOut},
        permissions=[IsOwnerProduct | IsAdminUser],
        auth=JWTAuth(),
    )
    def update_product_img(self, product_id: int, file: File[UploadedFile]):
        return crud.update_img_product(product_id, file)

    @route.patch(
        "/{product_id}",
        response={200: ProductOut},
        permissions=[IsOwnerProduct | IsAdminUser],
        auth=JWTAuth(),
    )
    def patch_product(self, product_id: int, product: PatchDict[PatchProduct]):
        return crud.patch_product(product_id, product)
