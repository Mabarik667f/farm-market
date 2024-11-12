from rest_framework import serializers

from api.v1.serializers.user_serializer import CustomUserSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField(min_value=1)
    count = serializers.IntegerField(min_value=1)
    about = serializers.JSONField()
    seller = CustomUserSerializer()

    class Meta:
        model = Product
        fields = ("id", "name", "price", "count", "about", "seller")
