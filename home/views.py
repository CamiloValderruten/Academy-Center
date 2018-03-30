from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from django.db import connection
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from tenant_users.tenants.tasks import provision_tenant
from . import forms

from core import models


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def features(request):
    return render(request, 'home/features.html')


def pricing(request):
    return render(request, 'home/pricing.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            schema = form.cleaned_data.pop('organization_schema')
            organization_name = form.cleaned_data.pop('organization_name')
            email = form.cleaned_data.pop('email')

            user = models.User.objects.create_user(email=email, password=form.cleaned_data.pop('password'))
            user.first_name = form.cleaned_data.pop('first_name')
            user.last_name = form.cleaned_data.pop('last_name')
            user.save()

            domain = provision_tenant(organization_name, schema, email)
            login(request, user)

            return HttpResponseRedirect("http://" + domain + '/dashboard')
        return HttpResponseBadRequest()

    if request.method == "GET":
        form = forms.RegisterForm()
        form.order_fields(['organization_name', 'first_name', 'last_name'])
        return render(request, 'authentication/register.html', dict(form=form))
