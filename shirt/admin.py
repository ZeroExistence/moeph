from django.contrib import admin

# Register your models here.

from .models import Shirt, Image, ShirtImage

admin.site.register(Shirt)
admin.site.register(ShirtImage)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('name','get_shirt', 'weight')