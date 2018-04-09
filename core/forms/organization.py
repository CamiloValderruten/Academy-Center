from django import forms
from .. import models
from django.core.mail import send_mail
from django.template.loader import get_template


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = models.Organization
        fields = ('name', 'day_start_time', 'day_end_time', 'logo')

    @staticmethod
    def send_welcome_email(user):
        if user.email:
            html = get_template('email/welcome.html').render(dict(user=user))
            send_mail(subject='Welcome to Academy Center', message='', html_message=html,
                      from_email='office@academycenter.com', recipient_list=[user.email])
