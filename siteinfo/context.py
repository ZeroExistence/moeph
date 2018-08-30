# This is a placeholder for siteinfo context. To follow.
from siteinfo.models import Navigation, SiteInfo
from django.http import Http404

def siteinfo(request):
	try:
		navigation_list = Navigation.on_site.filter(submenu__isnull=True)
		site_info = SiteInfo.objects.get(site__id=request.site.id)
	except:
		return {'request': request}
		#raise Http404
	return {'request': request,
		'navigation_list': navigation_list,
		'site_info': site_info}