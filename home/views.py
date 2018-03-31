from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseBadRequest
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
            organization = models.Organization(name=form.cleaned_data.pop('organization_name'))
            organization.save()
            user = models.Administrator.objects.create_user(organization=organization, **form.cleaned_data)
            login(request, user)
            return redirect('dashboard:index')
        return HttpResponseBadRequest()

    if request.method == "GET":
        form = forms.RegisterForm()
        form.order_fields(['organization_name', 'first_name', 'last_name'])
        return render(request, 'authentication/register.html', dict(form=form))
