from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from cart.models import CartItem
from api.v1.serializers.cart_serializer import CartItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (AllowAny,)
