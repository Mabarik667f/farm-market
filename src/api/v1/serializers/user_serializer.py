from django.contrib.auth.password_validation import validate_password
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


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    img = serializers.ImageField(required=False)

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
                regex=r'7(\d{10})',
                message="Введите номер телефона в Российском формате",
                code="invalid_registration"
            )
        ]
    )

    class Meta:
        model = Profile
        fields = "__all__"
