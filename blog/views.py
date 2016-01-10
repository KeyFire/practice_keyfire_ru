# coding: utf-8
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render, render_to_response, get_object_or_404, RequestContext
from django.template.context_processors import csrf
from blog.models import Article, Tag, UserLikes

tab_title = 'Блог Михаила Попова'


def all_articles(request):
    articles = Article.objects.published()
    return render_to_response('entry.html', {'articles': articles, 'tab_title': tab_title},
                              context_instance=RequestContext(request))


def articles_by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    articles = Article.objects.filter(tags=tag, publish=True)
    args = dict()
    args['articles'] = articles
    args['tab_title'] = u'Статьи по рубрике: {0}'.format(tag.title)
    args['title'] = u'Статьи по рубрике: {0}'.format(tag.title)

    return render_to_response('entry.html', args, context_instance=RequestContext(request))


def one_article(request, art_id):
    article = get_object_or_404(Article, pk=art_id)
    return render(request, 'post.html', {'object': article, 'tab_title': article.title},
                  context_instance=RequestContext(request))


def one_article_by_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    prev_article = Article.objects.filter(id=(article.id + 1))
    next_article = Article.objects.filter(id=(article.id - 1))
    args = dict()
    args['object'] = article
    args['tab_title'] = article.title
    args['prev_article'] = prev_article
    args['next_article'] = next_article
    args.update(csrf(request))

    return render(request, 'post.html', args, context_instance=RequestContext(request))


def add_like(request, slug):
    try:
        article = get_object_or_404(Article, slug=slug)
        user = auth.get_user(request)
        if user.is_authenticated():
            user_likes = UserLikes.objects.filter(user_id=user.id, article_id=article.id)
            if user_likes.count() == 0:
                article.likes += 1
                article.save()
                UserLikes(user=user, article=article, like=True).save();
            return redirect('/blog/%s/' % article.slug)
        else:
            rated = request.COOKIES.get(slug+"#like");
            if rated != None:
                return redirect('/blog/%s/' % article.slug)
            else:
                article.likes += 1
                article.save()
                response = redirect('/blog/%s/' % article.slug)
                response.set_cookie(slug+"#like", 1)
                return response
    except ObjectDoesNotExist:
        return Http404


def add_dislike(request, slug):
    try:
        article = get_object_or_404(Article, slug=slug)
        user = auth.get_user(request)
        if user.is_authenticated():
            user_likes = UserLikes.objects.filter(user_id = user.id, article_id = article.id)
            if user_likes.count() == 0:
                article.dislikes += 1
                article.save()
                UserLikes(user=user, article=article, dislike=True).save();
            return redirect('/blog/%s/' % article.slug)
        else:
            rated = request.COOKIES.get(slug+"#dislike");
            if rated != None:
                return redirect('/blog/%s/' % article.slug)
            else:
                article.dislikes += 1
                article.save()
                response = redirect('/blog/%s/' % article.slug)
                response.set_cookie(slug+"#dislike", 1)
                return response
    except ObjectDoesNotExist:
        return Http404


def pages(request, page_number=1):
    articles = Article.objects.published()
    current_page = Paginator(articles, 5)

    return render_to_response('page_entry.html',
                              {'articles': current_page.page(page_number),
                               'tab_title': tab_title},
                              context_instance=RequestContext(request))


def all_tags(request):
    tags_for_view = []
    tags = Tag.objects.all()
    for tag in tags:
        art_by_tags = Article.objects.filter(tags=tag, publish=True)
        if art_by_tags.count() > 0:
            el = dict()
            el['tag'] = tag
            el['count'] = art_by_tags.count()
            tags_for_view.append(el)
    args = dict()
    args['tab_title'] = u'Рубрики блога'
    args['title'] = u'Рубрики блога'
    args['objects'] = tags_for_view

    return render_to_response('tags.html', args, context_instance=RequestContext(request))
