#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import UserProfileAPIView

app_name = 'account'

urlpatterns = [

    re_path(r'^users/self$', UserProfileAPIView.as_view()),
]
