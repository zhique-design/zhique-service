#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page'
