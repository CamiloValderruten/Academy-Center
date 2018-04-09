import os
import sys

DEBUG = True
ADMINS = (
    ('Camilo Valderruten', 'camilovalderruten@gmail.com'),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MANAGERS = ADMINS

SECRET_KEY = '&l*n+hhw3g5-8a(6e-4v)-asf^_be=$lq^l*6*b#dbqm-$wag@'
ALLOWED_HOSTS = ['*']

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

INSTALLED_APPS = (
    'core',
    'home',
    'dashboard',
    'report',
    'attendance',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    "pinax.stripe",
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'pinax.stripe.middleware.ActiveSubscriptionMiddleware',
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
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'academycenter',
        'USER': 'camilo',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

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
LOGIN_URL = 'home:login'
LOGOUT_REDIRECT_URL = 'home:login'

STATIC_URL = '/static/'
DEFAULT_FROM_EMAIL = "support@academycenteronline.com"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_USE_TLS = True

ROOT_URLCONF = 'AcademyCenter.urls'
AUTH_USER_MODEL = 'core.User'

PINAX_STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_TEST_PUBLIC_KEY", "pk_test_jf5SLi86O7gMZf0L9QHj6bzq")
PINAX_STRIPE_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "sk_test_guwfnJ833HK37cYpkpteHxxE")
PINAX_STRIPE_DEFAULT_PLAN = 'basic'
PINAX_STRIPE_SUBSCRIPTION_REQUIRED_REDIRECT = 'dashboard:index'


STRIPE_LIVE_PUBLIC_KEY = os.environ.get("STRIPE_LIVE_PUBLIC_KEY", "pk_live_wRJkslkT2WzEiala8ypPlyD0")
STRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "sk_live_qdIw1RqPJLmjB2yutRrgSO2f")

SITE_ID = 1
