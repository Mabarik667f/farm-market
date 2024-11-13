from rest_framework import serializers

from product.models import Product
from user.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField(min_value=1)
    count = serializers.IntegerField(min_value=1)
    about = serializers.JSONField()

    # change query set to seller
    seller = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Product
        fields = ("id", "name", "price", "count", "about", "seller")
