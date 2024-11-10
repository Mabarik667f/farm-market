from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import CustomUser

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
        user: CustomUser = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            name=validated_data["username"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
