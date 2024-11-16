from ninja_extra import permissions, ControllerBase
from django.http import HttpRequest

from user.models import RoleForUser


class IsSeller(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, controller: ControllerBase) -> bool:
        r = RoleForUser.objects.filter(user_id=request.user.pk, role__name="S").select_related('role')
        return True if r else False


class IsOwnerProduct(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, controller: ControllerBase) -> bool:
        r = RoleForUser.objects.filter(user_id=request.user.pk, role__name="S").select_related('role')
        return True if r else False
