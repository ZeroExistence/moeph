from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

# Create your views here.

from .models import Shirt, ShirtImage, Image

def shirt_all(request):
	shirt_list = Shirt.on_site.all().order_by('name')
	paginator = Paginator(shirt_list, 30)
	page = request.GET.get('page')
	#context = {'book_list': paginator.get_page(page),
	context = {'shirt_list': shirt_list,
				'all_details': True}

	return render(request, 'shirt/shirt_list.html', context)


class ShirtDetailView(generic.DetailView):
	model = Shirt

	def get_object(self):
 		try:
 			return Shirt.on_site.get(code=self.kwargs['shirt'])
 		except Shirt.DoesNotExist:
 			raise Http404()

