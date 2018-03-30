from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, TemplateView
from django.contrib.auth import login

from core import models
from . import forms


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = models.Administrator.objects.filter().all()
        return context


class ApplicationView(FormView):
    title = 'Register for an Account'
    template_name = 'authentication/register.html'
    form_class = forms.ParentRegisterForm

    def form_valid(self, form):
        parent = models.Parent.objects.create_user(**form.cleaned_data)
        form.send_email()
        login(self.request, parent.user)
        return redirect('dashboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ModelListView(ListView):
    title = 'List'
    template_name = 'dashboard/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class AdministratorListView(ModelListView):
    title = 'Administrator'
    model = models.Administrator


class TeacherListView(ModelListView):
    title = 'Teacher'
    model = models.Teacher


class ParentListView(ModelListView):
    title = 'Parent'
    model = models.Teacher


class StudentListView(ModelListView):
    title = 'Student'
    model = models.Teacher
