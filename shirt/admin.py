from django.contrib import admin

# Register your models here.

from .models import Shirt, Image, ShirtImage

admin.site.register(Shirt)
admin.site.register(ShirtImage)
admin.site.register(Image)