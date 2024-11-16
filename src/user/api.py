import logging
from django.db import connection
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from user.schemas import AddRole, Register, UserOut, UserOutWithEmail
from user.models import CustomUser, RoleForUser, Role as RoleModel

from ninja_extra import ControllerBase, api_controller, route, permissions

logger = logging.getLogger('cons')

@api_controller('/users', tags=['users'], permissions=[])
class UserAPI(ControllerBase):
    @route.post('/register', response={201: UserOutWithEmail}, permissions=[])
    def register(self, payload: Register):
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

        user = CustomUser.objects.get(username=payload.username)
        return user

    @route.get('/{user_id}', response={200: UserOut}, permissions=[])
    def get_user(self, user_id: int):
        user = get_object_or_404(CustomUser, id=user_id)
        return user


    @route.delete('/{user_id}', response={204: None})
    def del_user(self, user_id: int):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()


    @route.post('/role/{user_id}', response={201: UserOut})
    def add_role(self, user_id: int, role: AddRole):
        role_obj = get_object_or_404(RoleModel, name=role.name)
        user = get_object_or_404(CustomUser, id=user_id)

        data = {
            "user_id": user_id,
            "role_id": role_obj.pk
        }
        data = list(data.values())
        template = ', '.join(["%s"] * len(data))
        with connection.cursor() as cursor:
            cursor.execute(f"CALL add_role_for_user({template})", data)

        user = get_object_or_404(CustomUser, id=user_id)
        return user


    @route.delete('/role/{user_id}', response={204: UserOut})
    def del_role(self, user_id: int, role: AddRole):
        role_obj = get_object_or_404(RoleModel, name=role.name)
        obj = get_object_or_404(RoleForUser, user_id=user_id, role_id=role_obj.pk)
        obj.delete()

        user = get_object_or_404(CustomUser, id=user_id)
        return user
