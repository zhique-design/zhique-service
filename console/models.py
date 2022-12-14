from django.db import models

from ZhiQue.mixins import BaseModelMixin


# Create your models here.
class Menu(BaseModelMixin):
    name = models.CharField('菜单名称', max_length=30, unique=True)
    path = models.CharField('菜单路径', blank=True, null=True, max_length=256)
    parent_menu = models.ForeignKey('self', verbose_name="父级菜单", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
