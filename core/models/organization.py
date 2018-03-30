from django.db import models
from tenant_users.tenants.models import TenantBase
from tenant_users.tenants.utils import create_public_tenant


class Organization(TenantBase):
    name = models.CharField(max_length=50, null=False, default=None)
    on_trial = models.BooleanField(default=True)
    trial_started_on = models.DateTimeField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    stripe_client_id = models.CharField(max_length=100, default=None, null=True)
