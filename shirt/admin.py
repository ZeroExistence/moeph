from django.contrib import admin

# Register your models here.

from .models import Shirt, Image

admin.site.register(Shirt)

admin.site.register(Image)
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
# 	list_display = ('shirt', 'note', 'weight')