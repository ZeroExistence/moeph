from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.

class SiteInfo(models.Model):
	name = models.CharField(max_length=50, help_text="Enter a book genre", unique=True)
	site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True, blank=True)
	banner = models.ImageField(upload_to='{0}/siteinfo/'.format(settings.MEDIA_ROOT), help_text="Original quality will be retained on upload.", null=True, blank=True)
	header = models.TextField(max_length=1000, help_text="This will be the site header", null=True, blank=True)
	description = models.TextField(max_length=1000, help_text="This will be the site description", null=True, blank=True)
	
	def __str__(self):
		return self.name

class Navigation(models.Model):
	name = models.CharField(max_length=100, help_text="Enter a book genre", unique=True)
	url = models.CharField(max_length=50, null=True, blank=True)
	site = models.ManyToManyField(Site, blank=True)
	weight = models.PositiveSmallIntegerField(default=9)
	submenu = models.ForeignKey('Navigation', on_delete=models.SET_NULL, null=True, blank=True)
	objects = models.Manager()
	on_site = CurrentSiteManager()

	class Meta:
		ordering = ['weight']

	def __str__(self):
		return self.name

	def get_submenu(self):
		return self.navigation_set.all()
