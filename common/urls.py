#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import CategorySelectOptionView

app_name = 'common'

urlpatterns = [
    re_path(r'category-select-options', CategorySelectOptionView.as_view(), name='category-select-options'),
]
