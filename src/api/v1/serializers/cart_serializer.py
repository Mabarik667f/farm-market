from rest_framework import serializers

from cart.models import CartItem
from product.models import Product
from user.models import CustomUser


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    count = serializers.IntegerField(min_value=1)
    delivery_date = serializers.DateTimeField()

    class Meta:
        model = CartItem
        fields = ("id", "user", "product", "count", "delivery_date")
