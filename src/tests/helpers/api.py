from cart.models import CartItem
from product.models import Product
from category.models import Category, CategoryHasProduct
from django.utils import timezone

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
