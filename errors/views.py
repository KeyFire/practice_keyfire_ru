# coding: utf-8

from django.shortcuts import render_to_response

# Create your views here.

title = 'Практикум по Python+Django'


def errors(request):
    header = 'Обработка ошибок'
    return render_to_response('errors.html', {'title': title, 'header': header})