#import django.contrib.sites.models
import string

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.http.request import split_domain_port
from django.utils.translation import gettext_lazy as _

SITE_CACHE = {}

from django.contrib.sites.models import *
from django.db import models


# Create your models here.

class CustomSite(Site):
	description = models.TextField(max_length=1000, null=True, blank=True)

	class Meta:
		db_table = 'django_site'
		verbose_name = _('site')
		verbose_name_plural = _('sites')
		ordering = ('domain',)