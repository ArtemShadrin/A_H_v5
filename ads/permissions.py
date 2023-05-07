from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = "У Вас нет доступа к этой подборке"

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author
        else:
            raise Exception("Неверно применен пермишн!")

        if request.user == owner:
            return True


class IsStaff(BasePermission):
    message = "Вы не являетесь модератором или администратором"

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
