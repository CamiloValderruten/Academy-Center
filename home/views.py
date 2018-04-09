from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import login
from core import models as core_models
from . import forms


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


class RegisterFormView(FormView):
    form_class = forms.RegisterForm
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        organization = core_models.Organization(name=form.cleaned_data.pop('organization_name'))
        organization.save()
        administrator = core_models.Administrator.objects.create_user(organization=organization, **form.cleaned_data)
        login(self.request, administrator)
        self.form_class.send_email(administrator)
        self.form_class.create_stripe_account(administrator, organization)
        return redirect('dashboard:index')
