# -*- coding: utf-8 -*-

from rest_framework import permissions

from .service import get_client_ip


class IsAuthor(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                or request.method == 'DELETE'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        ip_addr = get_client_ip(request)
        return obj.guest == ip_addr or obj.owner == request.user
