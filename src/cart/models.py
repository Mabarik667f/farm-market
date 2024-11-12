from django.db import models


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to="user.CustomUser", on_delete=models.CASCADE)
    product = models.ForeignKey(to="product.Product", on_delete=models.CASCADE)

    count = models.PositiveIntegerField(default=1)
    delivery_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()
