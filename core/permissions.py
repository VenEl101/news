from rest_framework import permissions
from rest_framework.permissions import BasePermission
from users.models import User



class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return True

        return user.is_superuser and user.role == User.Roles.ADMIN



class IsAdmin(BasePermission):
    def has_permission(self, request, view):

        user = request.user
        return user.is_authenticated and user.role == User.Roles.ADMIN