from django.db import models


class Category(models.Model):
    name = models.CharField()
    products = models.ManyToManyField(
        to="product.Product",
        through="CategoryHasProduct",
        related_name='categories',
        related_query_name="category"
    )

    objects = models.Manager()


class CategoryHasProduct(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    product = models.ForeignKey(to="product.Product", on_delete=models.CASCADE)

    objects = models.Manager()
