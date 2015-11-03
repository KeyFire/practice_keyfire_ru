# coding: utf-8

from django.conf.urls import url
import errors.views as views

urlpatterns = [
    url(r'^$', views.errors),
]
