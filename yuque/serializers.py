#!/usr/bin/python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'xuzhao'
__email__ = 'xuzhao@zhique.design'

from abc import ABC

from rest_framework import serializers

from .models import Book, Doc


class BookSerializer(serializers.ModelSerializer):
    """仓库序列化"""
    class Meta:
        model = Book
        fields = '__all__'


class DocSerializer(serializers.ModelSerializer):
    """文章序列化"""
    class Meta:
        model = Doc
        fields = '__all__'


class BookHookSerializer(serializers.Serializer):
    """仓库hook序列化"""
    id = serializers.IntegerField()
    slug = serializers.SlugField()
    name = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DocHookSerializer(serializers.Serializer):
    """文章hook序列化"""

    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.SlugField()
    book_id = serializers.IntegerField()
    book = BookHookSerializer()
    body = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        Book.objects.update_or_create(validated_data['book'], id=validated_data['book_id'])
        del validated_data['book']
        doc, _ = Doc.objects.update_or_create(validated_data, id=validated_data['id'])
        return doc




