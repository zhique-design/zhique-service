#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .viewsets import MenuViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'menus', MenuViewSet)

app_name = 'console'

urlpatterns = [] + router.urls

