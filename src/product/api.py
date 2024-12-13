import logging
from django.http import HttpRequest
from ninja import File, PatchDict, UploadedFile
from ninja.pagination import paginate
from ninja_extra import ControllerBase, api_controller, route
from ninja_extra.permissions.common import IsAdminUser
from ninja_jwt.authentication import JWTAuth

from product.permissions import IsOwnerProduct, IsSeller
from product.schemas import CreateProduct, PatchProduct, ProductOut
from product import crud

logger = logging.getLogger("cons")

@api_controller(tags=["products"])
class ProductAPI(ControllerBase):
    @route.post("/", response={201: ProductOut}, permissions=[IsSeller])
    def create_product(self, product: CreateProduct, file: File[UploadedFile]):
        request: HttpRequest = self.context.request #type: ignore
        return crud.create_product(request.user.pk, product, file)

    @route.delete(
        "/{product_id}",
        response={204: None},
        permissions=[IsOwnerProduct | IsAdminUser]
    )
    def del_product(self, product_id: int):
        crud.del_product(product_id)

    @route.get("/{product_id}", response={200: ProductOut}, auth=None)
    def get_product(self, product_id: int):
        return crud.get_product(product_id)

    @route.get("/", response={200: list[ProductOut]}, auth=None)
    @paginate
    def list_products(self, category_ids: list[int] = []):
        return crud.list_products(category_ids)

    @route.put("/{product_id}/{cat_id}", response={201: ProductOut})
    def add_category_for_product(self, product_id: int, cat_id: int):
        return crud.add_category_for_product(product_id, cat_id)

    @route.delete("/{product_id}/{cat_id}", response={200: ProductOut})
    def del_category_for_product(self, product_id: int, cat_id: int):
        return crud.del_category_for_product(product_id, cat_id)

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
        return crud.patch_product(product_id, payload, file)
