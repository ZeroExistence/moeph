from django.contrib import admin

# Register your models here.

from .models import Genre, Book, Author, Volume, Tag

admin.site.register(Author)
admin.site.register(Tag)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title','genre', 'volume_count', 'site')
	list_filter = ('genre', 'featured')

	fieldsets = (
		('Book Details', {
			'fields': (('title','author'),'summary', 'site')
			}),
		('Book Categorization', {
			'fields': (('genre','featured'),'tag')
			})
		)

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
	list_display = ('title','volume', 'inventory', 'price')
	list_filter = ('title__genre', 'inventory')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ('name', 'site')