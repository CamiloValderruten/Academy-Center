import os
import sys

DEBUG = True
ADMINS = (
    ('Camilo Valderruten', 'camilovalderruten@gmail.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, os.pardir)

SECRET_KEY = '&l*n+hhw3g5-8a(6e-4v)-asf^_be=$lq^l*6*b#dbqm-$wag@'
ALLOWED_HOSTS = ['*']

SHARED_APPS = (
    'tenant_schemas',
    'home',
    'core',
    'tenant_users.permissions',
    'tenant_users.tenants',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'tenant_users.permissions',
    'dashboard',
)

AUTHENTICATION_BACKENDS = (
    'tenant_users.permissions.backend.UserBackend',
)

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'  # Tenant
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

INSTALLED_APPS = (
    'core',
    'home',
    'dashboard',
    'tenant_schemas',
    'tenant_users.permissions',
    'tenant_users.tenants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
)

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',  # Tenant
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.OrganizationMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AcademyCenter.wsgi.application'

DATABASES = {
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'academycenter',
        'HOST': 'localhost',
        'USER': 'root',
    },
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'academycenter',
        'USER': 'camilo',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',  # Tenant
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'dashboard:index'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

STATIC_URL = '/static/'
DEFAULT_FROM_EMAIL = "support@academycenteronline.com"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_USE_TLS = True


ROOT_URLCONF = 'AcademyCenter.urls.urls_organization'
PUBLIC_SCHEMA_URLCONF = 'AcademyCenter.urls.urls_public'  # Tenant
TENANT_MODEL = "core.Organization"  # Tenant
AUTH_USER_MODEL = 'core.User'
TENANT_USERS_DOMAIN = "localhost"
SESSION_COOKIE_DOMAIN = '.localhost'
