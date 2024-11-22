import logging
from datetime import timezone
from ninja_extra import ControllerBase, api_controller, route
from ninja_jwt.authentication import JWTAuth
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db import connection, transaction

from cart.models import CartItem
from config.exceptions import InsufficientProductError
from order.models import Order, History as HistoryModel
from order.permissions import IsOrderOwner
from order.schemas import CreateOrder, History, OrderOut, get_order_out_schema


logger = logging.getLogger('cons')

@api_controller("/orders", tags=["orders"], permissions=[], auth=JWTAuth())
class OrderAPI(ControllerBase):

    @route.post("/", response={201: OrderOut})
    def create_order(self, payload: CreateOrder):
        user = self.context.request.user #type: ignore
        order_data = {
            "user_id": user.pk,
            "address": payload.address,
            "phone": payload.phone,
            "created": payload.created
        }
        order_data_ls = list(order_data.values())
        order_template = ", ".join(["%s"] * len(order_data_ls))
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(f"CALL create_order({order_template})", order_data_ls)
                obj = Order.objects.get(created=payload.created.replace(tzinfo=timezone.utc), user_id=user.pk)

                cart_items = CartItem.objects.filter(id__in=payload.cart_item_ids).select_related("product")
                for item in cart_items:
                    if item.count > item.product.count:
                        raise InsufficientProductError()
                    item_data = {
                        "order_id": obj.pk,
                        "product_id": item.pk,
                        "count": item.count,
                        "delivery_date": item.delivery_date
                    }
                    data = list(item_data.values())
                    item_template = ", ".join(["%s"] * len(data))
                    cursor.execute(f"CALL create_order_item({item_template})", data)
                    item.product.count -= item.count
                    item.product.save()

        return get_order_out_schema(obj)


    @route.delete("/{order_id}", response={204: None}, permissions=[IsOrderOwner])
    def cancel_order(self, order_id: int):
        order = Order.objects.get(id=order_id)
        order.delete()

    @route.get('/{order_id}', response={200: OrderOut}, permissions=[IsOrderOwner])
    def get_order(self, order_id: int):
        order = Order.objects.get(id=order_id)
        return get_order_out_schema(order)

    @route.get("/history/all", response={200: list[History]})
    def get_all_history(self):
        user = self.context.request.user #type: ignore
        all_history = get_list_or_404(HistoryModel, profile_id=user.pk)
        return all_history
