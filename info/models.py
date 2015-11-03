# coding: utf-8

from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):  # Статьи
    class Meta:
        db_table = 'app_info_articles'

    # Описание модели
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True)
    date = models.DateTimeField(verbose_name='Добавлено')

    def __unicode__(self):
        return u'{0}'.format(self.title)


class Video(models.Model):  # Видео
    class Meta:
        db_table = 'app_info_video'
        ordering = ['-date']

    # Описание модели
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True)
    date = models.DateTimeField(verbose_name='Добавлено')
    thumbnail = models.CharField(verbose_name='Эскиз', max_length=200, default='')
    video_url = models.CharField(verbose_name='URL видео', max_length=200, default='')

    def __unicode__(self):
        return self.title


class Audio(models.Model):  # Аудио
    class Meta:
        db_table = 'app_info_audio'

    # Описание модели
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True)
    date = models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)

    def __unicode__(self):
        return self.title


# coding: utf-8
from django.db import models


class Incident(models.Model):  # Обращения
    class Meta:
        db_table = 'app_info_incidents'
        ordering = ['-date']

    # Перечисление типов обращений
    INCIDENT_TYPES = (
        ('CN', 'Консультация'),
        ('ER', 'Ошибка'),
        ('SG', 'Пожелание'),
    )
    # Описание модели
    number = models.IntegerField(verbose_name='Номер', default=0, unique=True)
    subject = models.CharField(verbose_name='Тема', max_length=200)
    description = models.TextField(verbose_name='Описание', blank=True,
                                   help_text='Если тема понятна, описание можно не указывать.')
    date = models.DateTimeField(verbose_name='Добавлено')
    type = models.CharField(verbose_name='Тип обращения', max_length=2,
                            default='CN', choices=INCIDENT_TYPES)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.number, self.subject, self.date)


class Post(models.Model):
    class Meta:
        db_table = 'app_info_post'
    content = RichTextField()
