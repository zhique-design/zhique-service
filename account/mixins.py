#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class PermissionsMixin(models.Model):
    """超级用户抽象模型"""
    is_superuser = models.BooleanField('超级用户状态', default=False, help_text='指明该用户缺省拥有所有权限。')

    class Meta:
        abstract = True
