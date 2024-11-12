from django.contrib.auth.password_validation import validate_password
from django.db import connection
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import CustomUser, Profile
from logging import getLogger

logger = getLogger("cons")

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(required=True, min_length=8, write_only=True,
        validators=[validate_password])
    password2 = serializers.CharField(required=True, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Пароли не совпадают!"})

        return attrs

    def create(self, validated_data) -> CustomUser:
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
        data = [*user_data.values()]
        with connection.cursor() as cursor:
            cursor.execute(f"CALL create_user({', '.join(['%s' for _ in range(len(data))])})", [*data])

        user = CustomUser.objects.get(username=validated_data["username"])

        return user


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    img = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = ("username", "email", "img")



class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    address = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(
        max_length=255,
        required=False,
        validators=[
            RegexValidator(
                regex=r'(^8|7\+7)(\d{10})',
                message="Введите номер телефона в Российском формате",
                code="invalid_registration"
            )
        ]
    )

    class Meta:
        model = Profile
        fields = "__all__"
