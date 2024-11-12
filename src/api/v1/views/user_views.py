from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from api.v1.serializers.user_serializer import CustomUserSerializer, RegisterSerializer
from user.models import CustomUser

class RegisterView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ["get", "post", "put", "patch", "delete"]
    permission_classes = (AllowAny,)
