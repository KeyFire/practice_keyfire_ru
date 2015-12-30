# coding: utf-8
from django.conf.urls import url
from blog.views import all_articles, one_article, one_article_by_slug, add_like, add_dislike, articles_by_tag, pages

urlpatterns = [
    url(r'^$', all_articles, name='all_articles'),
    url(r'^(?P<art_id>\d+)$', one_article, name='one_article'),
    url(r'^tags/(?P<slug>\S+)/$', articles_by_tag, name='articles_by_tag'),
    url(r'^pages/(\d+)/$', pages, name='pages'),
    url(r'^(?P<slug>\S+)/addlike/$', add_like, name='add_like'),
    url(r'^(?P<slug>\S+)/adddislike/$', add_dislike, name='add_dislike'),
    url(r'^(?P<slug>\S+)/$', one_article_by_slug, name='one_article_by_slug'),

]
