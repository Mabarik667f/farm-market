from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    mass = models.FloatField(default=0.0)
    shelf_life = models.DateField()
    about = models.JSONField()
    img = models.ImageField(upload_to="product/")

    seller = models.ForeignKey(to="user.Profile", on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(
        to="user.CustomUser",
        through="cart.CartItem",
        related_name="products",
        related_query_name="product",
    )

    objects = models.Manager()

    def get_upload_path(self):
        return f"{settings.MEDIA_ROOT}/"
