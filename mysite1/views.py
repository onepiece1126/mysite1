# -*- coding:utf-8 -*-

from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import time
from django.contrib import auth

from django import forms
from django.contrib.auth.forms import UserCreateForm
from django.http import HttpResponseRedirect

def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
    now=datetime.datetime.now()

    # html = "<html><body>It is now %s.</body></html>" %now

    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date':now}))
    
    # return HttpResponse(html)

    # return render_to_response('current_datetime.html', {'current_date':now})
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def hours_ahead(request,offset):
    try:
        offset = int(offset)

    except ValueError:
        raise Http404

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html="<html><body>In %s hours(s), it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)

def login_view(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/account/loginin/")
    else:
        return HttpResponseRedirect("/account/invalid/")

def register(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if forms.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreateForm()
    return render_to_response("registration/register.html", {"form":form,})