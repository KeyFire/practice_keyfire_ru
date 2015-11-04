# coding: utf-8
from django.db import models

class Article(models.Model):
    class Meta:
        db_table = 'app_modelsform_article'

    title = models.CharField(verbose_name='Заголовок', max_length=128)
    text = models.TextField(verbose_name='Текст', blank=True)

    def __unicode__(self):
        return self.title

