from django.db import connection
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from user.schemas import AddRole, Register
from user.models import CustomUser, RoleForUser, Role as RoleModel

def create_user(payload: Register) -> CustomUser:
    user_data = {
        "username": payload.username,
        "email": payload.email,
        "password": make_password(payload.password),
        "is_active": True,
        "is_staff": False,
        "is_superuser": False,
        "date_joined": timezone.now(),
        "first_name": "",
        "last_name": "",
        "img": "/"
    }
    data = list(user_data.values())
    template = ", ".join(["%s"] * len(data))
    with connection.cursor() as cursor:
        cursor.execute(f"CALL create_user({template})", data)

    return CustomUser.objects.get(username=payload.username)


def get_user(user_id: int) -> CustomUser:
    return get_object_or_404(CustomUser, id=user_id)


def add_role(user_id: int, role: AddRole):
    role_obj = get_object_or_404(RoleModel, name=role.name)

    data = {"user_id": user_id, "role_id": role_obj.pk}
    data = list(data.values())
    template = ', '.join(["%s"] * len(data))
    with connection.cursor() as cursor:
        cursor.execute(f"CALL add_role_for_user({template})", data)


def del_role(user_id: int, role: AddRole):
    role_obj = get_object_or_404(RoleModel, name=role.name)
    obj = get_object_or_404(RoleForUser, user_id=user_id, role_id=role_obj.pk)
    obj.delete()
