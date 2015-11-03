# coding: utf-8

from django.contrib import admin
from info.models import Article, Audio, Video, Incident, Post


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'subject', 'type', 'description')

admin.site.register(Article)
admin.site.register(Audio)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Post)
admin.site.register(Video)
