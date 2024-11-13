from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    img = models.ImageField(upload_to="users/")
    roles = models.ManyToManyField(
        to="Role",
        through="RoleForUser",
        related_name="users",
        related_query_name="user"
    )


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(
        RegexValidator(
            regex=r'7(\d{10})',
            message="Введите номер телефона в Российском формате",
            code="invalid_registration"
        ),
        null=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(phone__regex=r'7(\d{10})'),
                name="profile_phone_valid_format"
            )
        ]

    objects = models.Manager()

class Role(models.Model):
    class RoleChoices(models.TextChoices):
        SELLER = "S", "seller"
        ADMIN = "A", "admin"
        DEFAULT = "D", "default"

    name = models.CharField(max_length=10, choices=RoleChoices)

    objects = models.Manager()

class RoleForUser(models.Model):
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        unique_together = ('role', 'user')
