import logging
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.authentication import JWTAuth

from order.permissions import IsOrderOwner
from order.schemas import CreateOrder, History, OrderOut, get_order_out_schema
from order import crud

logger = logging.getLogger('cons')

@api_controller("/orders", tags=["orders"], permissions=[], auth=JWTAuth())
class OrderAPI(ControllerBase):

    @route.post("/", response={201: OrderOut})
    def create_order(self, payload: CreateOrder):
        user = self.context.request.user #type: ignore
        obj = crud.create_order(user.pk, payload)
        return get_order_out_schema(obj)

    @route.delete("/{order_id}", response={204: None}, permissions=[IsOrderOwner])
    def cancel_order(self, order_id: int):
        crud.cancel_order(order_id)

    @route.get('/{order_id}', response={200: OrderOut}, permissions=[IsOrderOwner])
    def get_order(self, order_id: int):
        order = crud.get_order(order_id)
        return get_order_out_schema(order)

    @route.get("/history/all", response={200: list[History]})
    def get_all_history(self):
        user = self.context.request.user #type: ignore
        return crud.get_all_history(user.pk)
