#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from django.urls import re_path
from .views import CategoryBreadcrumbView
from .viewsets import ArticleViewSet, CategoryViewSet, HotArticleViewSet, TagViewSet, RecommendArticleViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'hot-articles', HotArticleViewSet)
router.register(r'recommend-articles', RecommendArticleViewSet)

app_name = 'blog'

urlpatterns = [
                  re_path(r'^category-breadcrumb$', CategoryBreadcrumbView.as_view())
              ] + router.urls

