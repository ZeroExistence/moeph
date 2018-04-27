import PIL
from PIL import Image as pilimage
from django.db import models
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import StringIO, BytesIO
from local import functions

# Create your models here.

def volume_directory_location(instance, filename):
	return 'page/{0}-{1}'.format(instance.id, filename)

class Page(models.Model):
	link = models.SlugField(max_length=50)
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title

class Image(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='{0}/page/'.format(settings.MEDIA_ROOT))
	thumbnail = models.ImageField(upload_to='{0}/page/'.format(settings.MEDIA_ROOT), null=True, blank=True)

	def get_image_url(self):
		if self.image:
			return self.image.url
		else:
			return ''

	def __str__(self):
		return self.name

	# def save(self, *args, **kwargs):
	# 	self.thumbnail = functions.resize(self.image, )

	# 	super(Image, self).save(*args, **kwargs)
