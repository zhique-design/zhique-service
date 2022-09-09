#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.urls import re_path
from django.urls import path

from .views import AttachmentUploadView, AttachmentDownloadView

app_name = 'attachment'

urlpatterns = [
    re_path(r'upload', AttachmentUploadView.as_view(), name='upload'),
    path(r'download/<uuid:attachment_id>', AttachmentDownloadView.as_view(), name='download'),
]
