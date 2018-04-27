from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'seccererer'

ROOT_URLCONF = 'moeph.urls.moephadmin'


INSTALLED_APPS += [
	'django.contrib.staticfiles']