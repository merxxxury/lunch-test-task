from rest_framework import permissions


class IsRestaurant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'RES':
            return True
        return False
