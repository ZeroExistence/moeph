from django.contrib import admin
from siteinfo.models import SiteInfo, Navigation

# Register your models here.

admin.site.register(SiteInfo)

@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
	list_display = ('name', 'submenu', 'weight')