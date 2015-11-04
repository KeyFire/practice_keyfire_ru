# coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from models import Article
from forms import ArticleForm


def article_name(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            form.save()
        return HttpResponseRedirect('redirect/')
    else:
        form = ArticleForm()

    return render(request, 'article.html', {'form': form})

def article_redirect(request):
    return render_to_response('redirect.html')