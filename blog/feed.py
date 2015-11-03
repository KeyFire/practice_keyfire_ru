# coding: utf-8
from django.contrib.syndication.views import Feed
from blog.models import Article


class LatestPosts(Feed):
    title = "Блог Михаила Попова"
    link = "/feed/"
    description = 'Выполнение практикума по курсу Python + Django + Продажи'

    def items(self):
        return Article.objects.published()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
