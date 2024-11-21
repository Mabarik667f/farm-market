import logging
from ninja_extra import ControllerBase, permissions
from django.http import Http404, HttpRequest
from django.shortcuts import get_object_or_404

from order.models import Order


logger = logging.getLogger("cons")

class IsOrderOwner(permissions.BasePermission):
    def has_permission(self, request: HttpRequest, controller: ControllerBase) -> bool:
        if hasattr(controller.context, "kwargs"):
            order_id = controller.context.kwargs.get("order_id")
            if order_id is not None:
                try:
                    order = get_object_or_404(Order, id=order_id)
                    return True if order.user.pk == request.user.pk else False
                except Http404:
                    return False
        return True
