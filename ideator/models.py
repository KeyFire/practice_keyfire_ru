# coding: utf-8

from django.db import models
from markdown import markdown
from mptt.models import MPTTModel, TreeForeignKey
from uuslug import slugify

# Create your models here.

class Visual(models.Model):
    class Meta:
        db_table = 'app_ideator_visuals'

    img = models.CharField(max_length=120, verbose_name='Файл картинки')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка')
    index = models.IntegerField(verbose_name='Индекс')

    def __unicode__(self):
        return self.title


class Constructor(models.Model):
    class Meta:
        db_table = 'app_ideator_constructors'

    title = models.CharField(max_length=120, verbose_name='Наименование')
    tooltip = models.TextField(verbose_name='Подсказка')
    body = models.TextField(verbose_name='Описание')
    examples = models.TextField(verbose_name='Примеры')
    body_html = models.TextField(editable=False)
    examples_html = models.TextField(editable=False)
    slug = models.CharField(verbose_name='Транслит', max_length=200, unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '../constructor/%s' % self.slug

    def save(self):
        self.slug = slugify(self.title)
        self.body_html = markdown(self.body)
        self.examples_html = markdown(self.examples)
        super(Constructor, self).save()


class Section(MPTTModel):
    title = models.CharField(max_length=120, verbose_name='Наименование')
    owner = models.ForeignKey(Constructor, verbose_name='Владелец')
    parent = TreeForeignKey('self', verbose_name='Родитель', limit_choices_to={'is_folder': True},
                            null=True, blank=True, related_name='children', db_index=True)
    is_folder = models.BooleanField(verbose_name='Это папка')

    class Meta:
        db_table = 'app_ideator_sections'
        order_with_respect_to = 'owner'

    def __unicode__(self):
        return self.title


class Idea(models.Model):
    class Meta:
        db_table = 'app_ideator_ideas'

    date = models.DateTimeField(verbose_name='Дата')
    name = models.CharField(max_length=120, verbose_name='Наименование')
    constructor = models.ForeignKey(Constructor, verbose_name='Конструктор')
    trick = models.TextField(verbose_name='Фишка бизнеса')

    def __unicode__(self):
        return u'{1} от {2}'.format(self.owner.name, self.date)
