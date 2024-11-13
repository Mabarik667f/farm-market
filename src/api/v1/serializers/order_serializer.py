from rest_framework import serializers

from api.v1.serializers.cart_serializer import CartItemSerializer
from api.v1.serializers.user_serializer import CustomUserSerializer, ProfileSerializer
from order.models import History, Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=255)
    user = CustomUserSerializer()
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "address", "phone", "user", "cart_items")


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    cart_item = CartItemSerializer()

    class Meta:
        model = OrderItem
        fields = ("order", "cart_item")


class OrderWithItemsSerializer(serializers.BaseSerializer):
    order = OrderSerializer()
    order_items = OrderItemSerializer(many=True, read_only=True)


class HistorySerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    profile = ProfileSerializer()

    class Meta:
        model = History
        fields = ("order", "profile")
