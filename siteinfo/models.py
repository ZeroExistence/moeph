from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings

# Create your models here.

class SiteInfo(models.Model):
	name = models.CharField(max_length=50, help_text="Enter a book genre", unique=True)
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True, blank=True)
	banner = models.ImageField(upload_to='{0}/siteinfo/'.format(settings.MEDIA_ROOT), help_text="Original quality will be retained on upload.", null=True, blank=True)
	header = models.CharField(max_length=100, help_text="This will be the site header", null=True, blank=True)
	description = models.TextField(max_length=1000, null=True, blank=True)
	
	def __str__(self):
		return self.name