from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.v1.serializers.user_serializer import RegisterSerializer
from user.models import CustomUser

class RegisterView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = CustomUser.objects.all()
