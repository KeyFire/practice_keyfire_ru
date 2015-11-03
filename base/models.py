# coding: utf-8

from django.db import models
from markdown import markdown


class Record(models.Model):
    class Meta:
        abstract = True
        ordering = ['add_date']

    title = models.CharField(verbose_name='Заголовок', max_length=200)
    add_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    upd_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    def __unicode__(self):
        return self.title


class Lesson(Record):
    class Meta:
        db_table = 'app_main_lesson'
        ordering = ['priority', 'add_date']

    new = models.BooleanField(verbose_name="Новое")
    updated = models.BooleanField(verbose_name="Обновлено")
    ref = models.CharField(verbose_name='Ссылка', max_length=200, blank=True)
    priority = models.IntegerField(verbose_name='Приоритет', default=100)


class Task(Record):
    class Meta:
        db_table = 'app_main_task'

    tab_title = models.CharField(verbose_name='Заголовок закладки', blank=True, max_length=200, default="")
    lesson = models.ForeignKey(Lesson, verbose_name="Урок")
    ref = models.CharField(verbose_name='Ссылка', max_length=200, unique=True)
    show_solution = models.BooleanField(verbose_name="Выводить решение")
    new = models.BooleanField(verbose_name="Новое", default=True)
    updated = models.BooleanField(verbose_name="Обновлено")
    social = models.BooleanField(verbose_name="Соц.сети", default=True)
    disqus = models.BooleanField(verbose_name="Disqus")


class TaskSolutionSection(Record):
    class Meta:
        db_table = 'app_main_task_section'
        ordering = ['order', 'add_date']

    SECTION_TYPES = (
        ('Text', 'Текст'),
        ('CodeHTML', 'Код на HTML'),
        ('CodePython', 'Код на Python'),
    )

    task = models.ForeignKey(Task, verbose_name="Задача")
    order = models.IntegerField(verbose_name='Порядок', default=0)
    collapsed = models.BooleanField(verbose_name="Свернутая", default=False)
    section_type = models.CharField(verbose_name='Тип блока', max_length=10, choices=SECTION_TYPES)
    description = models.TextField(verbose_name='Описание')
    annotation = models.TextField(verbose_name='Комментарий', blank=True)
    annotation_HTML = models.TextField(editable=False)

    def save(self):
        annotation = self.annotation.replace('</event>', '</span>')
        annotation = annotation.replace('<event>', '<span class="text-info">'
                                                   '<span class="glyphicon glyphicon-calendar"></span> ')
        self.annotation_HTML = markdown(annotation)
        super(TaskSolutionSection, self).save()
