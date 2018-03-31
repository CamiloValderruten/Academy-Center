from django import forms
from django.forms.widgets import PasswordInput, EmailInput, DateInput
from core.models import User, Teacher, Administrator, Parent, Student
from django.contrib.auth import forms as auth_forms


class UserCreationForm(auth_forms.UserCreationForm):
    password1 = None
    password2 = None

    def send_welcome_email(self, user):
        pass

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class UserForm(auth_forms.UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class AdministratorForm(UserForm):
    class Meta:
        model = Administrator
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class TeacherForm(UserForm):
    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class ParentForm(UserForm):
    class Meta:
        model = Parent
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class StudentForm(UserForm):
    class Meta:
        model = Student
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'gender', 'avatar', 'phone_number', 'date_of_birth']


class ApplicationForm(forms.Form):
    field_order = ['organization_name', 'first_name', 'last_name']
    username = forms.CharField(label='Username', max_length=30, required=True)
    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.CharField(widget=EmailInput(), label='Email', required=True)
    password = forms.CharField(widget=PasswordInput(), label='Password', required=True)
