#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model

from account.admin import UserAdmin

User = get_user_model()

admin_site = AdminSite(name='admin')
admin_site.register(User, UserAdmin)