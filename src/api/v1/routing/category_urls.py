from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.category_views import CategoryViewSet, CategoryHasProductViewSet

category_router = DefaultRouter()
category_router.register(r'', CategoryViewSet, basename="category")

category_has_product_router = DefaultRouter()
category_has_product_router.register(r'', CategoryHasProductViewSet, basename="category-has-product")

urlpatterns = [
    path("", include(category_router.urls)),
    path("has-product/", include(category_has_product_router.urls)),
]
