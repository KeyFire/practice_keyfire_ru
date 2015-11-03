# coding: utf-8

from django.contrib import admin
from models import Lesson, Task, TaskSolutionSection


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'ref', 'show_solution', 'social', 'disqus', 'new', 'updated')

class TaskSolutionSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'collapsed', 'order', 'task', 'section_type', 'add_date')
    list_filter = ['task']

admin.site.register(Lesson)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskSolutionSection, TaskSolutionSectionAdmin)
