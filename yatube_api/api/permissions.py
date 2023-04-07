"""API permissions"""

from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Allow access only to object author."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
