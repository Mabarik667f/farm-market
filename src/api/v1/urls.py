from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView,
    SpectacularRedocView)


urlpatterns = [
    path("user/", include("api.v1.routing.user_urls")),
    path("product/", include("api.v1.routing.product_urls")),
    path("category/", include("api.v1.routing.category_urls")),
    path("cart/", include("api.v1.routing.cart_urls")),
    path("order/", include("api.v1.routing.order_urls")),

    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="api/v1"),
        name="schema"
    ),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui"
    ),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc"
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
