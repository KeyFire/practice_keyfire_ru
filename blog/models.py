# coding: utf-8
from django.db import models
from base.models import Record
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


class Tag(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = 'раздел'
        verbose_name_plural = 'Разделы'

    title = models.CharField(verbose_name="Имя", max_length=200, unique=True)
    slug = models.SlugField(verbose_name='Транслит', max_length=200, unique=True)

    def __unicode__(self):
        return self.title


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Article(Record):
    class Meta:
        db_table = 'app_blog_article'
        ordering = ['-add_date']
        verbose_name = 'статью блога'
        verbose_name_plural = 'Статьи блога'

    publish = models.BooleanField(verbose_name='Публиковать', default=True)
    body = RichTextUploadingField(verbose_name="Текст статьи", blank=True)
    subtitle = RichTextUploadingField(verbose_name="Анонс статьи", blank=True)
    description = models.TextField(verbose_name="Описание для RSS", blank=True)
    slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True, unique=True)  # ссылки не должны повторяться
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    likes = models.IntegerField(verbose_name='Нравится', default=0)
    dislikes = models.IntegerField(verbose_name='Не нравится', default=0)

    objects = ArticleQuerySet.as_manager() # Используется для выборки только опубликованных статей

    def get_absolute_url(self):
        return '/blog/%s/' % self.slug

class UserLikes(models.Model):
    class Meta:
        db_table = 'app_blog_user_likes'
        verbose_name = 'оценку пользователя'
        verbose_name_plural = 'Оценки пользователей'
    UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
    user = models.ForeignKey(UserModel, verbose_name="Пользователь")
    article = models.ForeignKey(Article, verbose_name="Статья")
    like = models.BooleanField(verbose_name="Нравится", default=False)
    dislike = models.BooleanField(verbose_name="Не нравится", default=False)


