from rest_framework import serializers

from api.v1.serializers.product_serializer import ProductSerializer
from category.models import Category, CategoryHasProduct

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "products")


class CategoryHasProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    category = CategorySerializer()

    class Meta:
        model = CategoryHasProduct
        fields = ("product", "category")
