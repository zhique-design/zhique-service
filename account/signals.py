#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

User = get_user_model()


@receiver(signals.post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    """
    创建用户信号量
    :param sender:
    :param instance: 实例
    :param created: 是否新建
    :param kwargs:
    :return:
    """
    if created:
        """创建用户时将明文密码改成加密格式"""
        password = instance.password
        instance.set_password(password)
        instance.save()