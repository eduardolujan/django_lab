# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import (login_required)
from django.http import (HttpResponse, HttpResponseRedirect, HttpRequest)
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import (render_to_response, render, redirect)
from .forms import UserProfileForm

try:
    import json
except ImportError:
    from django.utils import simplejson as json


def index(request):
    return HttpResponse('Text')


def login(request):
    template_name = 'angle/login.html'
    data_response = {}
    response = render_to_response(
        template_name,
        context_instance=RequestContext(
            request,
            data_response
        )
    )
    return HttpResponse(response)

from django.contrib.auth import authenticate
def register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        user_profile_form = UserProfileForm(data)
        if user_profile_form.is_valid():
            user_profile_form.save(commit=False)
            user_profile = user_profile_form.instance
            user_profile.save()
            return HttpResponse('Is valid')
        else:
            user_profile_form.errors
            pass
        HttpResponse('')
    template_name = 'angle/register.html'
    data_response = {}
    response = render_to_response(
        template_name,
        context_instance=RequestContext(
            request,
            data_response
        )
    )
    return HttpResponse(response)
