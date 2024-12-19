import logging
from ninja_extra import permissions, ControllerBase
from django.http import HttpRequest

from product.models import Product
from user.models import RoleForUser

logger = logging.getLogger("cons")


class IsSeller(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, controller: ControllerBase) -> bool:
        r = RoleForUser.objects.filter(
            user_id=request.user.pk, role__name="S"
        ).select_related("role")
        return True if r else False


class IsOwnerProduct(IsSeller):
    def has_permission(self, request: HttpRequest, controller: ControllerBase) -> bool:
        u = Product.objects.only("seller_id").filter(
            id=controller.context.kwargs.get("product_id")
        )
        return (
            True and super().has_permission(request, controller)
            if u[0].seller.pk == request.user.pk
            else False
        )
