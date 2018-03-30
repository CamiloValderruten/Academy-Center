

from . import urls_public, urls_organization

urlpatterns = urls_public.urlpatterns + urls_organization.urlpatterns
