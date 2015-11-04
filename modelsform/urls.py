# coding: utf-8
from django.conf.urls import include, patterns, url
from views import article_name, article_redirect

urlpatterns = [
    url(r'^$', article_name),
    url(r'^redirect/$', article_redirect),
]