# coding: utf-8

from django.shortcuts import render, render_to_response
from myforms.forms import MyNameForm
from django.http import HttpResponseRedirect

title = 'Практикум по Python+Django'

def my_name(request):
    title = 'Работа с формами'
    if request.method == 'POST':
        form = MyNameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/forms/tranks/')

    else:
        form = MyNameForm()

    return render(request, 'forms.html', {'title': title, 'form': form})


def myredirect(request):
    title = 'Успешная отправка формы'
    return render_to_response('trunk.html', {'title': title})
