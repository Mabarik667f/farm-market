from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from api.v1.views.user_views import ProfileViewSet, RegisterView, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

profile_router = DefaultRouter()
profile_router.register(r'', ProfileViewSet, basename='profile')

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls)),
    path("profiles/", include(profile_router.urls))
]
