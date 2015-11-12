# coding: utf-8
from django.conf.urls import url
from views import sign_in, sign_out


urlpatterns = [
    url(r'^signin/$', sign_in, name='signin'),
    url(r'^signout/$', sign_out, name='signout'),
]