from django.db import connection
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from api.v1.serializers.user_serializer import CustomUserSerializer, ProfileSerializer, RegisterSerializer
from user.models import CustomUser, Profile

class RegisterView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        validated_data = serializer.validated_data

        user_data = {
            "username": validated_data["username"],
            "email": validated_data["email"],
            "password": make_password(validated_data["password"]),
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "date_joined": timezone.now(),
            "first_name": "",
            "last_name": "",
            "img": ""
        }
        data = list(user_data.values())
        template = ", ".join(['%s'] * len(data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_user({template})", [*data])
        serializer.istance = self.get_queryset().get(username=validated_data["username"])


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "put", "patch", "delete"]
    permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ["get", "patch"]
    permission_classes = (AllowAny,)
