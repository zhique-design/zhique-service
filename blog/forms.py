#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from zhique_markdown.widgets import AdminMarkdownWidget

from .models import Article


class ArticleForm(forms.ModelForm):
    body = forms.CharField(widget=AdminMarkdownWidget())

    class Meta:
        model = Article
        fields = '__all__'
