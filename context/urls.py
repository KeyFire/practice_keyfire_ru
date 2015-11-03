# coding: utf-8

from django.conf.urls import url
from context.views import details, press_list, latest, my_template, fav_color
from django.views.generic import TemplateView

urlpatterns = [
     url(r'^details/(?P<art2id>\d+)/$', details),
     url(r'^list/$', press_list),
     url(r'^my_template/$', my_template),
     url(r'^fav_color/$', fav_color),
     url(r'^latest/$', latest),
     url(r'^about/', TemplateView.as_view(template_name='about.html'))
]
