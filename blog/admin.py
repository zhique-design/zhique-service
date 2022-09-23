from django.contrib import admin

from .forms import ArticleForm


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('id', 'title', 'created_time')
    list_display_links = ('title',)
