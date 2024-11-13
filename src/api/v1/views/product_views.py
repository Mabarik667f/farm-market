from django.db import connection
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from product.models import Product
from api.v1.serializers.category_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (AllowAny,)


    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        template = ", ".join(["%s"] * len(validated_data))

        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_product({template})")

        serializer.instance = self.get_queryset().get(
            name=validated_data["name"],
            seller_id=validated_data["seller_id"]
        )
