from django.db import connection
from django.shortcuts import get_object_or_404
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.authentication import JWTAuth

from cart.models import CartItem
from cart.schemas import AddCartItem, CartItemOut


@api_controller("/cart", tags=["cart"], auth=JWTAuth())
class CartAPI(ControllerBase):

    @route.post("/",  response={201: CartItemOut})
    def add_to_cart(self, cart: AddCartItem):

        dict_data = {
            "product_id": cart.product_id,
            "user_id": self.context.request.user.pk, #type: ignore
            "count": cart.count,
            "delivery_date": cart.delivery_date
        }

        data = list(dict_data.values())
        template = ", ".join(["%s"] * len(data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_cart_item({template})", data)
        obj = CartItem.objects.get(product_id=dict_data["product_id"], user_id=dict_data["user_id"])
        return obj

    @route.delete("/{cart_item_id}", response={204: None})
    def un_cart(self, cart_item_id: int):
        obj = get_object_or_404(CartItem, id=cart_item_id)
        obj.delete()

    @route.get('/', response={200: list[CartItemOut]})
    def get_cart(self):
        user_id = self.context.request.user.pk #type: ignore
        return CartItem.objects.filter(user_id=user_id)
