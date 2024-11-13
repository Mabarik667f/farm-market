from rest_framework import serializers

from api.v1.serializers.product_serializer import ProductSerializer
from category.models import Category, CategoryHasProduct
from product.models import Product

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ("id", "name", "products")


class CategoryHasProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = CategoryHasProduct
        fields = ("product", "category")
