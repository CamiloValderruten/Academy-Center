from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, FormView, TemplateView, UpdateView
from django.contrib.auth import login, forms as auth_forms
from django.contrib import messages

from core.models import User, Administrator, Teacher, Parent, Student
from . import forms


class DashboardView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administrators'] = Administrator.objects.for_organization(self.request.user.organization).all()
        return context


class ApplicationView(FormView):
    title = 'Register for an Account'
    template_name = 'authentication/register.html'
    form_class = forms.ApplicationForm

    def form_valid(self, form):
        parent = Parent.objects.create_user(**form.cleaned_data)
        form.send_email()
        login(self.request, parent.user)
        return redirect('dashboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


"""
User List Views
"""


class UserListView(ListView):
    template_name = 'dashboard/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['role'] = getattr(self, 'model').role
        return context

    def get_queryset(self):
        return super(UserListView, self).get_queryset().filter(organization=self.request.user.organization)


class AdministratorListView(UserListView):
    model = Administrator


class TeacherListView(UserListView):
    model = Teacher


class ParentListView(UserListView):
    model = Parent


class StudentListView(UserListView):
    model = Student


"""
User Creation Views
"""


class UserCreationView(FormView):
    form_class = forms.UserCreationForm
    template_name = 'dashboard/user/create.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserCreationView, self).get_context_data()
        context['role'] = getattr(self.model, 'role')
        return context

    def form_valid(self, form):
        user = self.model.objects.create_user(organization=self.request.user.organization, **form.cleaned_data)
        form.send_welcome_email(user)
        messages.success(self.request, 'User created.')
        self.success_url = reverse('dashboard:' + getattr(self.model, 'role'), args=[str(user.id)])
        return super(UserCreationView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There seemed to be a problem." + str(form.errors))
        return super(UserCreationView, self).form_invalid(form)


class AdministratorCreationView(UserCreationView):
    model = Administrator


class TeacherCreationView(UserCreationView):
    model = Teacher


class ParentCreationView(UserCreationView):
    model = Parent


class StudentCreationView(UserCreationView):
    model = Student


"""
User Edit Views
"""


class UserView(UpdateView):
    model = User
    template_name = 'dashboard/user/profile.html'
    form_class = forms.UserForm

    def get_queryset(self):
        return super().get_queryset().filter(organization=self.request.user.organization)

    def form_valid(self, form):
        messages.success(self.request, 'User updated.')
        return super(UserView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error!')
        return super(UserView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['reset_change_form'] = auth_forms.PasswordChangeForm(user=self.object)
        return context


class AdministratorView(UserView):
    model = Administrator
    template_name = 'dashboard/user/profile.html'
    form_class = forms.AdministratorForm


class TeacherView(UserView):
    model = Teacher
    template_name = 'dashboard/user/profile.html'
    form_class = forms.TeacherForm


class ParentView(UserView):
    model = Parent
    template_name = 'dashboard/user/parent.html'
    form_class = forms.ParentForm

    def get_context_data(self, **kwargs):
        context = super(ParentView, self).get_context_data(**kwargs)
        context['all_students'] = Student.objects.filter(organization=self.request.user.organization).all()
        return context


class StudentView(UserView):
    model = Student
    template_name = 'dashboard/user/student.html'
    form_class = forms.StudentForm

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['all_parents'] = Parent.objects.filter(organization=self.request.user.organization).all()
        return context
