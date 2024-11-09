from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    about = models.JSONField()

    seller = models.ForeignKey(to="user.Profile", on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(
        to="user.CustomUser",
        through="cart.CartItem",
        related_name="products",
        related_query_name="product"
    )
