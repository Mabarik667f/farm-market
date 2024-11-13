from django.db import connection
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from order.models import Order, History
from api.v1.serializers.order_serializer import OrderSerializer, OrderWithProductsSerializer, HistorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ["post", "get", "delete"]
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == "GET":
            serializer_class = OrderWithProductsSerializer
        return serializer_class

    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        data = {
            "address": validated_data["address"],
            "phone": validated_data["phone"],
            "user_id": validated_data["user_id"]
        }
        order_template = ', '.join(["%s"] * len(data))

        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_order({order_template}")
            order_id = Order.objects.only(id).get(user_id=data["user_id"]).order_by("-id")[0]
            for product in validated_data["order_items"]:
                item_data = {
                    "order_id": order_id,
                    "product_id": product["product"],
                    "count": product["count"],
                    "delivery_date": product["delivery_date"]
                }
                order_item_template = ', '.join(["%s"] * len(item_data))
                cursor.execute(f"CALL create_order_item({order_item_template}")

        serializer.instance = self.get_queryset().get(id=order_id)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    http_method_names = ["get"]
    permission_classes = (AllowAny,)
