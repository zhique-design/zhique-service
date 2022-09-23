#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model

from account.admin import UserAdmin
from blog.admin import CategoryAdmin, TagAdmin, ArticleAdmin
from blog.models import Category, Tag, Article

User = get_user_model()

admin_site = AdminSite(name='admin')
admin_site.register(User, UserAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Tag, TagAdmin)
admin_site.register(Article, ArticleAdmin)