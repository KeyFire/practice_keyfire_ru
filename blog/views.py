# coding: utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect, render, render_to_response, get_object_or_404, RequestContext
from blog.models import Article, Tag


def all_articles(request):
    articles = Article.objects.published()
    return render_to_response('entry.html', {'articles': articles, 'tab_title': 'Блог Михаила Попова'},
                              context_instance=RequestContext(request))


def articles_by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    articles = Article.objects.filter(tags=tag)


    return render_to_response('entry.html', {'articles': articles,
                                             'tab_title': u'Статьи по рубрике: {0}'.format(tag.title),
                                             'title': u'Статьи по рубрике: {0}'.format(tag.title)},
                              context_instance=RequestContext(request))


def one_article(request, art_id):
    article = get_object_or_404(Article, pk=art_id)
    return render(request, 'post.html', {'object': article, 'tab_title': article.title},
                  context_instance=RequestContext(request))


def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'post.html', {'object': article, 'tab_title': article.title},
                  context_instance=RequestContext(request))


def add_like(request, slug):
    try:
        article = get_object_or_404(Article, slug=slug)
        article.likes += 1
        article.save()
    except ObjectDoesNotExist:
        return Http404
    return redirect(request.GET.get('next', '/'))


def add_dislike(request, slug):
    try:
        article = get_object_or_404(Article, slug=slug)
        article.dislikes += 1
        article.save()
    except ObjectDoesNotExist:
        return Http404
    return redirect(request.GET.get('next', '/'))
