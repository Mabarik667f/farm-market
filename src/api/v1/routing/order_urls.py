from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.order_views import OrderViewSet, OrderItemViewSet, HistoryViewSet

order_router = DefaultRouter()
order_router.register(r'', OrderViewSet, basename="order")

order_item_router = DefaultRouter()
order_item_router.register(r'', OrderItemViewSet, basename="order-item")

history_router = DefaultRouter()
history_router.register(r'', HistoryViewSet, basename="history")

urlpatterns = [
    path("", include(order_router.urls)),
    path("order-item/", include(order_item_router.urls)),
    path("history/", include(history_router.urls))
]
