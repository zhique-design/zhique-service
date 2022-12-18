#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from blog.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        ref_name = 'CommonCategory'
        fields = ('id', 'name')
