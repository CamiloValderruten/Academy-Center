from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.db import connection
from . import models

from tenant_schemas.middleware import DefaultTenantMiddleware


class OrganizationMiddleware(DefaultTenantMiddleware):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        connection.set_schema(request.tenant.schema_name, include_public=True)
        return self.get_response(request)
