#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model

from account.admin import UserAdmin
from blog.admin import CategoryAdmin, TagAdmin
from blog.models import Category, Tag

User = get_user_model()

admin_site = AdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)