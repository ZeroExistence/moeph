from django.contrib import admin

# Register your models here.

from .models import Shirt, Image, Inventory, Credit, Link

admin.site.register(Shirt)

#admin.site.register(Image)
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	list_display = ('shirt', 'note', 'weight')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
	list_display = ('shirt', 'size', 'stock')

admin.site.register(Credit)
admin.site.register(Link)