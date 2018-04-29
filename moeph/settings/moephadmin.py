from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'seccererer'

ROOT_URLCONF = 'moeph.urls.moephadmin'

WSGI_APPLICATION = 'moeph.wsgi.moephadmin.application'

INSTALLED_APPS += [
	'django.contrib.staticfiles']

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