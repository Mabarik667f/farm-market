from rest_framework import serializers

from api.v1.serializers.product_serializer import ProductSerializer
from api.v1.serializers.user_serializer import CustomUserSerializer, ProfileSerializer
from cart.models import CartItem
from order.models import History, Order
from user.models import CustomUser
from product.models import Product


class OrderItem(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    count = serializers.IntegerField(min_value=1)
    delivery_date = serializers.DateTimeField()

    class Meta:
        model = CartItem
        fields = ("product", "count", "delivery_date")


class OrderItemWithProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    count = serializers.IntegerField(min_value=1)
    delivery_date = serializers.DateTimeField()

    class Meta:
        model = CartItem
        fields = ("product", "count", "delivery_date")


class OrderSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    address = serializers.CharField(max_length=255)
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    order_items = OrderItem(many=True)

    class Meta:
        model = Order
        fields = ("id", "address", "phone", "user_id", "order_items")


class OrderWithProductsSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    address = serializers.CharField(max_length=255)
    user = CustomUserSerializer()
    products = OrderItemWithProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "address", "phone", "user", "products")



class HistorySerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = History
        fields = ("order", "profile")
