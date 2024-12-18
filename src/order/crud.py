import logging
from datetime import timezone
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db import connection, transaction

from cart.models import CartItem
from user.models import Profile
from config.exceptions import InsufficientProductError
from order.models import Order, History
from order.schemas import CreateOrder


logger = logging.getLogger('cons')

def create_order(user_id: int, payload: CreateOrder) -> Order:

    profile_id = Profile.objects.get(user_id=user_id).pk
    order_data = {
        "user_id": profile_id,
        "address": payload.address,
        "phone": payload.phone,
        "created": payload.created
    }
    order_data_ls = list(order_data.values())
    order_template = ", ".join(["%s"] * len(order_data_ls))
    with transaction.atomic():
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_order({order_template})", order_data_ls)
            obj = Order.objects.get(created=payload.created.replace(tzinfo=timezone.utc), user_id=user_id)

            cart_items = CartItem.objects.filter(id__in=payload.cart_item_ids).select_related("product")
            if not cart_items:
                raise InsufficientProductError()
            for item in cart_items:
                if item.count > item.product.count:
                    raise InsufficientProductError()
                item_data = {
                    "order_id": obj.pk,
                    "product_id": item.product.pk,
                    "count": item.count,
                    "delivery_date": item.delivery_date
                }
                data = list(item_data.values())
                item_template = ", ".join(["%s"] * len(data))
                cursor.execute(f"CALL create_order_item({item_template})", data)
                item.product.count -= item.count
                item.product.save()
                item.delete()
    return obj


def cancel_order(order_id: int) -> None:
    get_order(order_id).delete()


def get_order(order_id: int) -> Order:
    return get_object_or_404(Order, id=order_id)


def get_all_history(user_id: int) -> list[History]:
    profile_id = Profile.objects.get(user_id=user_id).pk
    return get_list_or_404(History, profile_id=profile_id)
