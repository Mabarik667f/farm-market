from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from order.models import Order, OrderItem, History
from api.v1.serializers.order_serializer import OrderSerializer, OrderItemSerializer, HistorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = (AllowAny,)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    http_method_names = ["get", "post"]
    permission_classes = (AllowAny,)

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    http_method_names = ["get"]
    permission_classes = (AllowAny,)
