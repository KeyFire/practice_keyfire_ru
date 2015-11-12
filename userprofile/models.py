# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural =  'профили'

    user = models.OneToOneField(User)
    website = models.URLField(verbose_name='Сайт', blank=True)

    def __unicode__(self):
        return self.user.username
