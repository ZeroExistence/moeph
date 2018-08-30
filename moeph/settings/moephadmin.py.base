from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'Chang3m3'

ROOT_URLCONF = 'moeph.urls.moephadmin'

WSGI_APPLICATION = 'moeph.wsgi.moephadmin.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

## Config Settings

MEDIA_URL = '/'
MEDIA_ROOT = 'media/'

INSTALLED_APPS += [
	'django.contrib.staticfiles']

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "../common/static"),
	]

## Site ID
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Chang3m3',
        'USER': 'Chang3m3',
        'PASSWORD': 'Chang3m3',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
