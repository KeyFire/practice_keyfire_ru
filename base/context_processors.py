# coding: utf-8

from models import Lesson, Task, TaskSolutionSection
from django.shortcuts import get_object_or_404


def dropdown_menu():
    menu_text = [u'<ul class="dropdown-menu">']
    lessons = Lesson.objects.all()
    first_block = True
    for lesson in lessons:
        if not first_block:
            menu_text.append(u'\n<li role="separator" class="divider"></li>')
        first_block = False
        if lesson.ref != "":
            menu_text.append(u'\n<li><a href="{0}">{1}'.format(lesson.ref, lesson.title))
            if lesson.new:
                menu_text.append(u' <span class="label label-danger">Новый</span>')
            elif lesson.updated:
                menu_text.append(u' <span class="label label-warning">Обновлено</span>')
            menu_text.append(u'</a></li>')
        tasks = Task.objects.filter(lesson_id=lesson)
        for task in tasks:
            menu_text.append(u'\n<li><a href="{0}">{1}'.format(task.ref, task.title))
            if task.new:
                menu_text.append(u' <span class="label label-danger">Новый</span>')
            elif task.updated:
                menu_text.append(u' <span class="label label-warning">Обновлено</span>')
            menu_text.append(u'</a></li>')
    menu_text.append(u'\n</ul>')
    return "".join(menu_text)


def menu():
    menu_text = []
    lessons = Lesson.objects.all()
    first_block = True
    for lesson in lessons:
        if not first_block:
            menu_text.append(u'\n')
        if lesson.ref == "":
            menu_text.append(u'\n<h4>{0}'.format(lesson.title))
        else:
            menu_text.append(u'\n<a href="{0}"><h4>{1}'.format(lesson.ref, lesson.title))
        if lesson.ref != "":
            menu_text.append(u'</a>')
        if lesson.new:
            menu_text.append(u' <span class="label label-danger">Новый</span>')
        elif lesson.updated:
            menu_text.append(u' <span class="label label-warning">Обновлено</span>')
        menu_text.append(u'</h4>')
        tasks = Task.objects.filter(lesson_id=lesson)
        first_block = False
        for task in tasks:
            menu_text.append(u'\n&nbsp;&nbsp;&nbsp;<a href="{0}">{1}</a>'.format(task.ref, task.title))
            if task.new:
                menu_text.append(u' <span class="label label-danger">Новый</span>')
            elif task.updated:
                menu_text.append(u' <span class="label label-warning">Обновлено</span>')
            menu_text.append(u'<br>')
    return "".join(menu_text)


def base(request):
    path = request.META['PATH_INFO']
    try:
        task = Task.objects.get(ref=request.META['PATH_INFO'])
    except:
        task = {}
    if task != {}:
        task_sections = TaskSolutionSection.objects.filter(task_id=task.id)
        title = task.title
        tab_title = task.tab_title
    else:
        task_sections = ()
        title = None
        tab_title = ""

    return {'dropdown_menu': dropdown_menu(), 'menu': menu(),
            'task': task, 'title': title, 'tab_title': tab_title, 'task_sections': task_sections}
