from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.order_views import OrderViewSet, HistoryViewSet

order_router = DefaultRouter()
order_router.register(r'', OrderViewSet, basename="order")

history_router = DefaultRouter()
history_router.register(r'', HistoryViewSet, basename="history")

urlpatterns = [
    path("", include(order_router.urls)),
    path("history/", include(history_router.urls))
]
