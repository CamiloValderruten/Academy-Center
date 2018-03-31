from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

from .models import User, Organization


class OrganizationAdmin(ModelAdmin):
    list_display = ('name', 'trial_started_on', 'created_on',)
    list_filter = ('on_trial',)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('groups__name', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(User, CustomUserAdmin)
