# coding: utf-8
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf


def sign_in(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(request.POST.get('next', '/'))
        else:
            args['login_error'] = 'Имя пользователя или пароль указаны неверно'
            return render_to_response('login.html', args,
                                      context_instance=RequestContext(request))
    else:
        return render_to_response('login.html', args,
                                  context_instance=RequestContext(request))

@login_required
def sign_out(request):
    auth.logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))

