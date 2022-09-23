#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import _user_has_module_perms, _user_has_perm
from django.db import models


class PermissionsMixin(models.Model):
    """超级用户抽象模型"""
    is_superuser = models.BooleanField('超级用户状态', default=False, help_text='指明该用户缺省拥有所有权限。')

    class Meta:
        abstract = True

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        """
        Return True if the user has any permissions in the given app label.
        Use simlar logic as has_perm(), above.
        """
        # Active superusers have all permissions.
        if self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)
