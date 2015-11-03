# coding: utf-8

from django.conf.urls import url
import info.views as views

urlpatterns = [
    # info:
    url(r'^hobby/$', views.hobby),
    url(r'^me/$', views.me),
    url(r'^project/$', views.project),
    url(r'^work/$', views.work),
    url(r'^help/$', views.help),
    url(r'^articles/$', views.articles),
    url(r'^video/$', views.video),
    url(r'^audio/$', views.audio),
    url(r'^posts/$', views.posts),
]
