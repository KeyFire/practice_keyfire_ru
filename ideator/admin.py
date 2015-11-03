# coding: utf-8

from django.contrib import admin
from ideator.models import Constructor, Section, Idea, Visual
from django_markdown.admin import MarkdownModelAdmin


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_folder', 'owner', 'parent')
    list_filter = ['owner']
    search_fields = ['title']


class VisualAdmin(admin.ModelAdmin):
    list_display = ('title', 'index', 'img')


class ConstructorAdmin(MarkdownModelAdmin):
    list_display = ('title', 'tooltip', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Visual, VisualAdmin)
admin.site.register(Constructor, ConstructorAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Idea)
