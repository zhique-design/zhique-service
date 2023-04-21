#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import viewsets

from ZhiQue import mixins, permissions
from blog.models import Category
from .models import Menu
from .serializers import MenuSerializer, CategorySerializer


class MenuViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(parent_menu__isnull=True)
        return self.queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                      mixins.ViewSetMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        if self.action == 'list':
            return super().get_queryset().filter(parent_category__isnull=True)
        return super().get_queryset()
