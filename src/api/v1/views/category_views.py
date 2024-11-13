from django.db import connection

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from category.models import Category, CategoryHasProduct
from api.v1.serializers.category_serializer import CategoryHasProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_category({validated_data["name"]}")

        serializer.instance = self.get_queryset().get(name=validated_data["name"])

class CategoryHasProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryHasProduct.objects.all()
    serializer_class = CategoryHasProductSerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        template = ", ".join(["%s"] * len(validated_data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_category_has_product({template}")

        serializer.instance = self.get_queryset().get(
            product_id=data["product_id"],
            category_id=data['category_id'])
