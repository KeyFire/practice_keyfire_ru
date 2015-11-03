# coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext
from blog.models import Article
from django.contrib.syndication.views import Feed


def all_articles(request):
    articles = Article.objects.published()
    return render_to_response('entry.html', {'articles': articles, 'tab_title': 'Блог Михаила Попова'}, context_instance=RequestContext(request))


def one_article(request, art_id):
    article = get_object_or_404(Article, pk=art_id)
    return render(request, 'post.html', {'article': article}, context_instance=RequestContext(request))


def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'post.html', {'article': article, 'tab_title': article.title},
                  context_instance=RequestContext(request))

