#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)
    parent_menu = serializers.IntegerField(source='parent_menu_id', write_only=True)

    @staticmethod
    def get_children(obj):
        queryset = Menu.objects.filter(parent_menu_id=obj.id)
        serializer = MenuSerializer(queryset, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = Menu
        fields = ('id', 'name', 'path',  'parent_menu', 'children')
