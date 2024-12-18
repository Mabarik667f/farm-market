from django.db import connection
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from cart.models import CartItem
from cart.schemas import AddCartItem
from product.models import Product
from config.exceptions import InsufficientProductError


def add_to_cart(user_id: int, cart: AddCartItem) -> CartItem:

    product = get_object_or_404(Product, id=cart.product_id)
    if product.count < cart.count:
        raise InsufficientProductError()

    dict_data = {
        "product_id": cart.product_id,
        "user_id": user_id,
        "count": cart.count,
        "delivery_date": cart.delivery_date
    }
    in_cart = CartItem.objects.filter(product_id=dict_data["product_id"], user_id=dict_data["user_id"])
    if not in_cart.exists():
        data = list(dict_data.values())
        template = ", ".join(["%s"] * len(data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_cart_item({template})", data)
    else:
        item: CartItem = in_cart.first() #type: ignore
        item.count += cart.count
        item.save()
    obj = CartItem.objects.get(product_id=dict_data["product_id"], user_id=dict_data["user_id"])
    return obj


def get_cart_item(cart_item_id: int) -> CartItem:
    return get_object_or_404(CartItem, id=cart_item_id)


def un_cart(cart_item_id: int) -> None:
    get_cart_item(cart_item_id).delete()


def get_cart(user_id: int) -> QuerySet[CartItem]:
    return CartItem.objects.filter(user_id=user_id)
