from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.cart_views import CartItemViewSet

router = DefaultRouter()
router.register(r'', CartItemViewSet, basename="cart")

urlpatterns = [
    path("", include(router.urls))
]
