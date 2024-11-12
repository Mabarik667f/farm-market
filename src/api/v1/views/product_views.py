from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from product.models import Product
from api.v1.serializers.category_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (AllowAny,)
