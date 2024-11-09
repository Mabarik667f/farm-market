from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="users/")
    roles = models.ManyToManyField(
        to="Role",
        through="RoleForUser",
        related_name="users",
        related_query_name="user"
    )

class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(
        RegexValidator(
            regex=r'(^8|7\+7)(\d{10})',
            message="Введите номер телефона в Российском формате",
            code="invalid_registration"
        )
    )


class Role(models.Model):
    class RoleChoices(models.TextChoices):
        SELLER = "S", "seller"
        ADMIN = "A", "admin"
        DEFAULT = "D", "default"

    name = models.CharField(max_length=10, choices=RoleChoices)


class RoleForUser(models.Model):
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
