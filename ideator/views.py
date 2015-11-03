# coding: utf-8

from django.shortcuts import render_to_response, RequestContext
from ideator.models import Constructor, Section, Visual


def vision(request):
    title = 'Визуализатор'
    visuals = Visual.objects.order_by('index').all()
    return render_to_response('vision.html',
                              {'title': title,
                               'visuals': visuals},
                              context_instance=RequestContext(request))


def constructors(request):

    constructors = Constructor.objects.order_by('title').all()
    title = ''

    return render_to_response('constructors.html',
                              {'title': title,
                               'constructors': constructors},
                              context_instance=RequestContext(request))


def constructor(request, slug):

    item = Constructor.objects.get(slug=slug)
    title = ''
    sections = Section.objects.filter(owner_id=item.id)

    return render_to_response('constructor.html',
                              {'title': title, 'tab_title': item.title + u" - Бизнес-конструкторы",
                               'item': item,
                               'nodes': sections},
                              context_instance=RequestContext(request))
