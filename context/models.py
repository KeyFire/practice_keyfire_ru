# coding: utf-8
from django.db import models


class PressRelease(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=120)

    class Meta:
        db_table = 'app_context_press_releases'
        get_latest_by = 'pub_date' # получение последнего объекта выполняется по полю pub_date

    def get_absolute_url(self):
        return '../details/%d' % self.id

    def __unicode__(self):
        return self.title


