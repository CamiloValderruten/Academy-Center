from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from django.conf import settings


urlpatterns = [

]


def public_reverse(viewname, args=None, kwargs=None, current_app=None):
    """
    You must to use this for public urls
    """
    return reverse(viewname, urlconf=settings.PUBLIC_SCHEMA_URLCONF, args=args, kwargs=kwargs, current_app=current_app)


def tenant_reverse(viewname, args=None, kwargs=None, current_app=None):
    """
    You must to use this for tenant urls
    """
    return reverse(viewname, urlconf=settings.ROOT_URLCONF, args=args, kwargs=kwargs, current_app=current_app)