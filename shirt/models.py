from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from common import functions

# Create your models here.

class Shirt(models.Model):
	code = models.SlugField(max_length=200, null=True, blank=True, editable=False)
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(max_length=2000, null=True, blank=True)
	featured = models.BooleanField(default=False)
	site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
	objects = models.Manager()
	on_site = CurrentSiteManager()

	def __str__(self):
		return self.name

	def is_featured(self):
		return self.featured

	def get_images(self):
		return self.image_set.all()

	def get_absolute_url(self):
		return reverse('shirt:shirt-detail', args=[str(self.code)])

	## For auto-slugify
	def save(self, *args, **kwargs):
		self.code = slugify(self.name)
		super(Shirt, self).save(*args, **kwargs)

	class Meta:
		ordering = ["name"]

class Image(models.Model):
	shirt = models.ForeignKey(Shirt, on_delete=models.SET_NULL, null=True, blank=True)
	note = models.CharField(max_length=200, null=True, blank=True)
	credits = models.TextField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='{0}/shirt/'.format(settings.MEDIA_ROOT), help_text="Images will be uploaded with original size", null=True, blank=True)
	weight = models.PositiveSmallIntegerField()
	landscape = models.BooleanField(default=True, editable=False)

	def __str__(self):
		if self.shirt:
			return '{0} - {1}'.format(self.shirt.name, self.weight)
		else:
			return '{0} - {1}'.format(self.note, self.weight)

	## For auto-slugify
	def save(self, *args, **kwargs):
		if self.image:
			self.landscape = functions.is_landscape(self.image)
		super(Image, self).save(*args, **kwargs)

	class Meta:
		ordering = ["shirt", "weight"]
