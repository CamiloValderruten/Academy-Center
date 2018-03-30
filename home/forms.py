from django import forms
from django.forms.widgets import PasswordInput, EmailInput

attributes = {"class": "form-control"}


class RegisterForm(forms.Form):
    organization_name = forms.CharField(label='Organization', max_length=30, required=True)
    organization_schema = forms.CharField(label='Organization Username', max_length=30, required=True)
    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.CharField(widget=EmailInput(), label='Email', required=True)
    password = forms.CharField(widget=PasswordInput(), label='Password', required=True)
