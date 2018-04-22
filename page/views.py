from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views import generic
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

from .models import Page
from book.models import Book, Genre
#import book.urls 

def index(request):
	current_site = get_current_site(request)
	featured_book = Book.objects.filter(site=current_site.id).filter(featured__exact=True)
	genre_list = Genre.objects.filter(site=current_site.id)

	#return render(request, 'page/page_detail.html', {'page': index_page})
	return render(request, 'index.html', {'featured_book': featured_book, 'genre_list': genre_list, 'current_site': current_site})


class PageView(generic.DetailView):
	model = Page

	def get_object(self):
		return get_object_or_404(Page, link=self.kwargs['link'])

