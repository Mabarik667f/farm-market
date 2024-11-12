from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from category.models import Category, CategoryHasProduct
from api.v1.serializers.category_serializer import CategoryHasProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = (AllowAny,)


class CategoryHasProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryHasProduct.objects.all()
    serializer_class = CategoryHasProductSerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = (AllowAny,)
