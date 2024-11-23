from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.authentication import JWTAuth

from cart.schemas import AddCartItem, CartItemOut
from cart import crud

@api_controller("/cart", tags=["cart"], auth=JWTAuth())
class CartAPI(ControllerBase):

    @route.post("/",  response={201: CartItemOut})
    def add_to_cart(self, cart: AddCartItem):
        return crud.add_to_cart(self.context.request.user.pk, cart) #type: ignore

    @route.delete("/{cart_item_id}", response={204: None})
    def un_cart(self, cart_item_id: int):
        crud.un_cart(cart_item_id)

    @route.get('/', response={200: list[CartItemOut]})
    def get_cart(self):
        return crud.get_cart(self.context.request.user.pk) #type: ignore
