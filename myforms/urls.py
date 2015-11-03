# coding: utf-8

from django.conf.urls import url
from myforms.views import my_name, myredirect

urlpatterns = [
    url(r'^$', my_name),
    url(r'^tranks/$', myredirect)
]