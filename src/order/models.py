from django.core.validators import RegexValidator
from django.db import models


class Order(models.Model):

    address = models.CharField(max_length=255)
    phone = models.CharField(
        RegexValidator(
            regex=r'(^8|7\+7)(\d{10})',
            message="Введите номер телефона в Российском формате",
            code="invalid_create_order"
        )
    )
    user = models.ForeignKey(
        to="user.CustomUser",
        on_delete=models.CASCADE,
        related_name="orders",
        related_query_name="order"
    )
    cart_items = models.ManyToManyField(
        to="cart.CartItem",
        through="OrderItem",
        related_name="orders",
        related_query_name="order"
    )

    created = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(phone__regex=r'(^8|7\+7)(\d{10})'),
                name="order_phone_valid_format"
            )
        ]



class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(to="cart.CartItem", on_delete=models.CASCADE)

    objects = models.Manager()

class History(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    profile = models.ForeignKey(to="user.Profile", on_delete=models.CASCADE)

    objects = models.Manager()
