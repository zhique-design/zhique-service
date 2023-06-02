#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from blog.models import Category
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)
    parent_menu = serializers.IntegerField(source='parent_menu_id', write_only=True, required=False)

    @staticmethod
    def get_children(obj):
        queryset = Menu.objects.filter(parent_menu_id=obj.id)
        serializer = MenuSerializer(queryset, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = Menu
        fields = ('id', 'name', 'path',  'parent_menu', 'children')


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)
    path = serializers.CharField(source='get_category_path', read_only=True)
    parent = serializers.JSONField(source='get_parent_category', read_only=True)
    parent_category = serializers.IntegerField(source='parent_category_id', write_only=True, required=False)

    @staticmethod
    def get_path(obj):
        return obj.get_category_path()

    @staticmethod
    def get_children(obj):
        queryset = obj.get_children()
        if queryset.count() == 0:
            return None
        serializer = CategorySerializer(queryset, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = Category
        ref_name = 'ConsoleCategory'
        fields = ('id', 'name', 'path', 'children', 'parent', 'parent_category')
