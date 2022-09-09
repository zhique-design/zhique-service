#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """只允许管理员用户访问"""

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_active and user.is_superuser)


class AllowAny(BasePermission):
    """允许任何人访问"""

    def has_permission(self, request, view):
        return True
