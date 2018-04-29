from .base import *

DEBUG = False

ALLOWED_HOSTS = ['moe.ph']

SECRET_KEY = 'seccererer'

ROOT_URLCONF = 'moeph.urls.moeph'

WSGI_APPLICATION = 'moeph.wsgi.moeph.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

## Config Settings

MEDIA_URL = '/'
MEDIA_ROOT = 'media/'

## Site ID
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'moeph',
        'USER': 'moeph',
        'PASSWORD': 'Chang3m3',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}