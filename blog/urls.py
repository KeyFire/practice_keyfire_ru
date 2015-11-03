# coding: utf-8
from django.conf.urls import url
from blog import feed
from blog.views import all_articles, one_article, one_article_by_slug

urlpatterns = [
    url(r'^$', all_articles, name='all_articles'),
    url(r'^(?P<art_id>\d+)$', one_article, name='one_article'),
    url(r'^(?P<slug>\S+)/$', one_article_by_slug, name='one_article_by_slug')
]
