from django import forms
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.template.loader import get_template
from django.forms.widgets import PasswordInput, EmailInput


attributes = {"class": "form-control"}


class RegisterForm(forms.Form):
    organization_name = forms.CharField(label='Organization Name', max_length=30, required=True)
    username = forms.CharField(label='Your Username', validators=[ASCIIUsernameValidator()], max_length=20, required=True)
    first_name = forms.CharField(label='First Name', max_length=20, required=True)
    last_name = forms.CharField(label='Last Name', max_length=20, required=True)
    email = forms.CharField(label='Email', widget=EmailInput(), required=True)
    password = forms.CharField(label='Password', widget=PasswordInput(), required=True)

    @staticmethod
    def send_email(administrator):
        html = get_template('email/welcome.html').render(dict(user=administrator))
        send_mail(subject='Welcome to Academy Center', message='', html_message=html,
                  from_email='welcome@academycenter.com', recipient_list=[administrator.email])

    @staticmethod
    def create_stripe_account(administrator, organization):
        pass
