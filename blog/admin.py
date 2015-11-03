# coding: utf-8
from django.contrib import admin
from models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'add_date', 'slug')
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)

