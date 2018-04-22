from django.contrib import admin

# Register your models here.

from .models import Page, Image

admin.site.register(Page)
#admin.site.register(Image)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'get_image_url')

# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
# 	fieldsets = (
# 		('Page Detail', {
# 			'fields': (('link','title'),'description')
# 			}),
# 		('Page Image', {
# 			'fields': ('image')
# 			})
# 		)
