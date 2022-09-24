#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import VERSION

from .views import upload_image
if VERSION < (1, 9):
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^uploadimage/$', upload_image),
    )
else:
    from django.conf.urls import url

    app_name = 'zhique_markdown'
    urlpatterns = [
        url(r'^uploadimage/$', upload_image),

    ]