from cart.models import CartItem
from order.models import Order, OrderItem
from product.models import Product
from category.models import Category, CategoryHasProduct
from django.utils import timezone

from user.models import CustomUser


def create_user(username: str, email: str) -> CustomUser:

    user_data = CustomUser.objects.create_user(
        username=username,
        email=email,
        password="1234"
    )
    return user_data


def create_product(seller_id: int, categories: list[Category]) -> Product:
    pr = Product.objects.create(
        name="string",
        price=1,
        count=1,
        about={"mass": 100},
        img="/",
        seller_id=seller_id
    )
    for cat in categories:
        CategoryHasProduct.objects.create(product_id=pr.pk, category_id=cat.pk)
    return pr


def create_cart_item(product_id: int, user_id: int) -> CartItem:
    return CartItem.objects.create(
        product_id=product_id,
        user_id=user_id,
        count=2,
        delivery_date=timezone.now()
    )


def create_order(user_id: int, cart_items: list[CartItem]) -> Order:
    order = Order.objects.create(
        user_id=user_id,
        phone="72833254670",
        address="Test address 123"
    )
    for cart_item in cart_items:
        OrderItem.objects.create(
            order_id=order.pk,
            product_id=cart_item.product.pk,
            count=cart_item.count,
            delivery_date=cart_item.delivery_date
        )

    return order
