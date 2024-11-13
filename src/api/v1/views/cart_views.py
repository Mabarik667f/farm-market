from django.db import connection
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from cart.models import CartItem
from api.v1.serializers.cart_serializer import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        template = ", ".join(["%s"] * len(validated_data))

        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_cart_item({template})")

        serializer.instance = self.get_queryset().get(
            user_id=validated_data["user_id"],
            product_id=validated_data["product_id"]
        )
