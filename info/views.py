# coding: utf-8
from django.shortcuts import render_to_response, Http404, RequestContext
from info.models import Article, Incident, Audio, Video, Post


def index(request): # Jumbotron
    return render_to_response('index.html', context_instance=RequestContext(request))


def hobby(request): # Увлечения
    return render_to_response('hobby.html', context_instance=RequestContext(request))


def me(request): # Обо мне
    return render_to_response('me.html', context_instance=RequestContext(request))


def work(request): # Мои работы
    return render_to_response('work.html', context_instance=RequestContext(request))


def project(request): # О Проекте
    total = 60
    finished = 48.0
    progress = int(round(finished/total*100,0))
    return render_to_response('project.html',
                              {'progress': progress, 'finished': int(finished), 'total': total},
                              context_instance=RequestContext(request))


def articles(request): # Статьи
    # Модель.менеджер.что_вывести()
    article = Article.objects.all()
    return render_to_response('articles.html', {'articles': article},
                              context_instance=RequestContext(request))


def help(request): # Работа с моделями
    # Модель.менеджер.что_вывести()
    incidents = Incident.objects.all()
    last2 = Incident.objects.order_by('-date')[0:2]
    record2 = Incident.objects.get(id=2)
    return render_to_response('help.html', {'incidents': incidents, 'last2': last2, 'record2': record2},
                              context_instance=RequestContext(request))


def video(request): # Видео
    # Модель.менеджер.что_вывести()
    videos = Video.objects.all()
    return render_to_response('video.html', {'videos': videos},
                              context_instance=RequestContext(request))


def audio(request): # Аудио
     # Модель.менеджер.что_вывести()
    audios = Audio.objects.all()
    return render_to_response('audio.html', {'audios': audios},
                              context_instance=RequestContext(request))


def posts(request): # Про шаблоны

    posts = Post.objects.all()
    return render_to_response('posts.html', {'posts': posts},
                              context_instance=RequestContext(request))


def pages(request, pg_num):
    try:
        pg_num = int(pg_num)
    except ValueError:
        raise Http404

    class Paginator():
        # Параметры пагинатора
        def __init__(self):
            self.pg_num = pg_num
        pg_count = 999 # максимальное количество страниц
        next_pg = min(pg_num + 1, pg_count)
        prev_pg = max(pg_num - 1, 1)
        pg_from = max(pg_num - 3, 1)
        if pg_from > 1:
            pg_from += 1
        pg_to = min(pg_from + 4, pg_count)

    title = 'Страница № {0}'.format(pg_num)
    return render_to_response('page.html', {'title':title, 'paginator': Paginator},
                              context_instance=RequestContext(request))

