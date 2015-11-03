# coding: utf-8
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from context.models import PressRelease
from django.shortcuts import get_object_or_404, get_list_or_404
from django.template import Context, Template, loader, RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response

title = 'Практикум к шагу 24'

"""
def details(request, art2id):
    return HttpResponse('Страница не существует')
"""
"""
def details(request, art2id):
    return HttpResponseServerError('Ошибка сервера')
"""
"""
def details(request, art2id):
    try:
        p = PressRelease.objects.get(id=art2id)
        return HttpResponse(p.title)
    except PressRelease.DoesNotExist:
        return HttpResponseNotFound('Не найдено')
"""
"""
def details(request, art2id):
    p = get_object_or_404(PressRelease, id=art2id)
    return HttpResponse(p.title)
"""
"""
def details(request, art2id):
    p = get_object_or_404(PressRelease, id=art2id)
    t = loader.get_template("details.html")
    c = Context({'press': p})
    return HttpResponse(t.render(c))
"""
"""
def details(request):
    c = Context({'fav_color': ['green', 'red', 'blue']})
    t = loader.get_template('inner\example.html')
    return HttpResponse(t.render(c))
"""
"""
def latest(request):
    p = PressRelease.objects.latest()  # тут не указываем поле, т.к. поле упорядочивания указано в get_latest_by
    t = loader.get_template('latest.html')
    c = Context({
        'title': p.title,
        'author': p.author,
        'date': p.pub_date,
        'link': p.get_absolute_url()
    })
    return HttpResponse(t.render(c))
"""
"""
def latest(request):
    p = PressRelease.objects.latest()
    title = p.title
    author = p.author
    date = p.pub_date
    link = p.get_absolute_url()
    t = loader.get_template('latest.html')
    c = Context(locals())
    return HttpResponse(t.render())
"""
"""
def latest(request):
    p = PressRelease.objects.latest()
    t = loader.get_template('latest.html')
    c = Context({
        'title': p.title,
        'author': p.author,
        'date': p.pub_date,
        'link': p.get_absolute_url()
    })
    c['mu'] = 'корова'
    return HttpResponse(t.render(c))
"""
"""
def latest(request):
    p = PressRelease.objects.latest()
    return render_to_response('latest1.html', {'press': p})
"""
"""
def latest(request):
    p = PressRelease.objects.latest()
    ren = render_to_string('latest1.html', {'press': p})
    return HttpResponse(ren)
"""
"""
def press_list(request):
    pl = get_list_or_404(PressRelease)
    t = loader.get_template("list.html")
    c = Context({'press_list': pl})
    return HttpResponse(t.render(c))
"""


def my_template(request):
    return render_to_response("my_template.html")

def addtest():
    return {'1': 'Вася','2': 'Петя', 'cp':[1,2,3,4]}


def my_test(request):
    c = Context(addtest())
    t = loader.get_template('my_test.html')
    template_art = t.render(c)
    return HttpResponse(template_art) # вернуть


def fav_color(request):
    my_dict = {'fav_color': 'Малиновый'}  # словарь со значением для подстановки
    my_template = 'Мой любимый цвет {{ fav_color }}' # шаблон с параметром
    c = Context(my_dict) # получение объекта контекста
    t = Template(my_template) # получение объекта шаблона
    rendered_template = t.render(c) # рендеринг шаблона (подстановка параметров в шаблон из контектса)
    return HttpResponse(rendered_template) # возврат результата рендеринга - готовая страница


def press_list(request):
    pl = get_list_or_404(PressRelease)
    t = loader.get_template("list.html")
    c = RequestContext(request, {'press_list': pl})
    return HttpResponse(t.render(c))


def details(request, art2id):
    p = get_object_or_404(PressRelease, id=art2id)
    c = RequestContext(request, {'press': p})
    return render_to_response("details.html", c)


def latest(request):
    p = PressRelease.objects.latest()
    return render_to_response('latest1.html',
                              {'press': p},
                              context_instance=RequestContext(request))
