from django.db import models
from markdownx.models import MarkdownxField
from django.utils.text import slugify
from markdownx.utils import markdownify
from django.utils import safestring

# Create your models here.

class Post(models.Model):
	code = models.SlugField(max_length=50, null=True, blank=True, editable=False)
	title = models.CharField(max_length=50, help_text="Enter blog title:", unique=True)
	body = MarkdownxField(max_length=1000, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		get_latest_by = 'created_at'

	## For auto-slugify of book_code fr0m title
	def save(self, *args, **kwargs):
		self.code = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def md_body(self):
		return safestring.mark_safe(markdownify(self.body))


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
