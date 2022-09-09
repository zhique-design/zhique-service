#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator(validators.RegexValidator):
    """用户名校验"""
    regex = r'^[a-zA-Z0-9_.]{4,16}$'
    message = '请输入4-16位字母数字以及下划线和点的组合'
    flags = 0