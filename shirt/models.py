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
	image = models.OneToOneField('ShirtImage', on_delete=models.CASCADE, primary_key=True)
	site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
	objects = models.Manager()
	on_site = CurrentSiteManager()

	def __str__(self):
		return self.name

	def is_featured(self):
		return self.featured

	## For auto-slugify
	def save(self, *args, **kwargs):
		self.code = slugify(self.name)
		super(Shirt, self).save(*args, **kwargs)

	class Meta:
		ordering = ["name"]

class Image(models.Model):
	code = models.SlugField(max_length=200, null=True, blank=True, editable=False)
	name = models.CharField(max_length=200, unique=True)
	credits = models.TextField(max_length=200, null=True, blank=True)
	image = models.ImageField(upload_to='{0}/shirt/'.format(settings.MEDIA_ROOT), help_text="Images will be uploaded with original size", null=True, blank=True)
	weight = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.name

	def get_shirt(self):
		return self.shirtimage_set.get(linked_images=self.id).name

	## For auto-slugify
	def save(self, *args, **kwargs):
		self.code = slugify(self.name)
		#if self.image:
		#	self.image = functions.resize(self.image, 1000,300)
		super(Image, self).save(*args, **kwargs)

	class Meta:
		ordering = ["weight", "name"]

class ShirtImage(models.Model):
	code = models.SlugField(max_length=200, null=True, blank=True, editable=False)
	name = models.CharField(max_length=200, unique=True)
	linked_images = models.ManyToManyField('Image')

	def __str__(self):
		return self.name

	## For auto-slugify
	def save(self, *args, **kwargs):
		self.code = slugify(self.name)
		super(ShirtImage, self).save(*args, **kwargs)