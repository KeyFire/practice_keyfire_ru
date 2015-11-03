# coding: utf-8

from django.conf.urls import url
from ideator.views import constructors, constructor, vision

urlpatterns = [
    url(r'^constructors/$', constructors, name='constructors'),
    url(r'^constructor/(?P<slug>\S+)/$', constructor, name='constructor'),
    url(r'^vision/$', vision, name='vision'),
]
