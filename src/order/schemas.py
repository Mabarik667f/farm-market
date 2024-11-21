from datetime import datetime
from pydantic import PositiveInt
from ninja import Schema
from ninja.schema import Field

from product.models import Product
from product.schemas import ProductOutForOrder
from order.models import Order as OrderModel, OrderItem

class Order(Schema):
    address: str  = Field(max_length=255)
    phone: str = Field(pattern=r"7(\d{10})")
    created: datetime = Field(default_factory=datetime.now)


class CreateOrder(Order):
    cart_item_ids: list[int] = Field(min_length=1)


class BaseOrderItem(Schema):
    count: PositiveInt = Field(gt=0)
    delivery_date: datetime


class OrderItemOut(BaseOrderItem):
    id: int
    product: ProductOutForOrder


class OrderOut(Order):
    id: int
    products: list[OrderItemOut] = Field(min_length=0)


class OrderOutForHistory(Order):
    id: int


class History(Schema):
    order: OrderOutForHistory
    profile_id: int = Field(gt=0)


def get_order_out_schema(order: OrderModel) -> OrderOut:
    order_items = OrderItem.objects.filter(order_id=order.pk)
    products = Product.objects.filter(id__in=[item.product.pk for item in order_items]).select_related("seller")
    products = [ProductOutForOrder(
        id=pr.pk,
        name=pr.name,
        price=pr.price,
        img=pr.img,
        seller=pr.seller)
        for pr in products]

    order_items_out = []

    for order_item, pr in zip(order_items, products):
        item = OrderItemOut(
            count=order_item.count,
            delivery_date=order_item.delivery_date,
            id=order_item.pk,
            product=pr
        )
        order_items_out.append(item)

    return OrderOut(
        address=order.address,
        phone=order.phone,
        id=order.pk,
        created=order.created,
        products=order_items_out
    )
