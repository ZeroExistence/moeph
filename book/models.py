from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from local import functions

# Functions for image path upload
def volume_directory_location(instance, filename):
	return '{0}/book/{1}-{2}'.format(settings.MEDIA_ROOT, instance.id, filename)

# Create your models here.

class Genre(models.Model):
	code = models.SlugField(max_length=50, null=True, blank=True, editable=False)
	name = models.CharField(max_length=50, help_text="Enter a book genre", unique=True)
	description = models.TextField(max_length=1000, null=True, blank=True)
	image = models.ImageField(upload_to='{0}/genre/'.format(settings.MEDIA_ROOT), help_text="Images to be uploaded here will be resized to 1000x300", null=True, blank=True)
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	objects = models.Manager()
	on_site = CurrentSiteManager()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.code = slugify(self.name)
		if self.image:
			self.image = functions.resize(self.image, 1000,300)
		super(Genre, self).save(*args, **kwargs)

	# def get_absolute_url(self):
	# 	return reverse('book-list')

class Book(models.Model):
	code = models.SlugField(max_length=200, null=True, blank=True, editable=False)
	title = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
	summary = models.TextField(max_length=1000, null=True, blank=True)
	genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
	tag = models.ManyToManyField('Tag')
	featured = models.BooleanField(default=False)
	site = models.ForeignKey(Site, on_delete=models.CASCADE)
	objects = models.Manager()
	on_site = CurrentSiteManager()

	def __str__(self):
		return self.title

	def display_tag(self):
		return ', '.join([ tag.name for tag in self.tag.all()[:10] ])

	def is_featured(self):
		return self.featured

	def volume_count(self):
		return self.volume_set.count()

	def get_first_volume_image(self):
		return self.volume_set.get(volume='1').image

	display_tag.short_description = 'Tag'

	## For auto-slugify of book_code fr0m title
	def save(self, *args, **kwargs):
		self.code = slugify(self.title)
		super(Book, self).save(*args, **kwargs)

	## This is to return the tags for reverse URL in template
	def get_tags(self):
		return self.tag.all()

	def get_absolute_url(self):
		return reverse('book:book-detail', args=[str(self.genre),str(self.code)])

	class Meta:
		ordering = ["title"]


class Author(models.Model):
	code = models.SlugField(max_length=200, null=True, blank=True, editable=False)
	name = models.CharField(max_length=200, unique=True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.code = slugify(self.name)

		super(Author, self).save(*args, **kwargs)

class Volume(models.Model):
	title = models.ForeignKey(Book, on_delete=models.CASCADE)
	volume = models.PositiveSmallIntegerField()
	alt_title = models.CharField(max_length=200, null=True, blank=True)
	price = models.PositiveSmallIntegerField()
	inventory = models.PositiveSmallIntegerField()
	image = models.ImageField(upload_to='{0}/volume/'.format(settings.MEDIA_ROOT), help_text="Images to be uploaded here will be resized to 400x600" , blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["title", "volume"]
		get_latest_by = 'updated_at'


	def __str__(self):
		if self.alt_title == "":
			return '{0} {1}'.format(self.title, self.volume)
		if not self.alt_title:
			return '{0} {1}'.format(self.title, self.volume)
		else:
			return '{0} {1} - {2}'.format(self.title, self.volume, self.alt_title)

	def get_availability(self):
		if self.inventory > 0:
			return "Available"
		elif self.inventory > 99:
			return "For Pre-Order"
		else:
			return "Out of Stock"

	def save(self, *args, **kwargs):
		if self.image:
			self.image = functions.resize(self.image, 400, 600)
		super(Volume, self).save(*args, **kwargs)

	def get_title(self):
		if self.alt_title == "":
			return '{0} {1}'.format(self.title, self.volume)
		if not self.alt_title:
			return '{0} {1}'.format(self.title, self.volume)
		else:
			return self.alt_title


class Tag(models.Model):
	code = models.SlugField(max_length=50, null=True, blank=True, editable=False)
	name = models.CharField(max_length=50, unique=True)


	def get_absolute_url(self):
		return reverse('book-tag', args=[str(self.book_code)])

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.code = slugify(self.name)

		super(Tag, self).save(*args, **kwargs)

