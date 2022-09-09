#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

User = get_user_model()


@receiver(signals.post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()