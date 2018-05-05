from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

# Create your views here.
from .models import Book, Genre, Author, Volume, Tag
from .forms import SearchForm


def book_all(request):
	book_list = Book.on_site.all().order_by('title')
	paginator = Paginator(book_list, 3)
	page = request.GET.get('page')
	context = {'book_list': paginator.get_page(page),
				'all_details': True}

	return render(request, 'book/book_list.html', context)


class BookListView(generic.ListView):
	model = Book

	def get_queryset(self):
		try:
			return Book.on_site.filter(genre__code__exact=self.kwargs['slug'])
		except Book.DoesNotExist:
			raise Http404()

	def get_context_data(self, **kwargs):
		context = super(BookListView, self).get_context_data(**kwargs)
		context.update({
			'genre_details': get_object_or_404(Genre, code=self.kwargs['slug'])
			})
		return context

	#paginate_by = 18


class BookDetailView(generic.DetailView):
	model = Book

	def get_object(self):
 		try:
 			return Book.on_site.get(genre__code=self.kwargs['genre'], code=self.kwargs['book'])
 		except Book.DoesNotExist:
 			raise Http404()


class BookTagView(generic.ListView):
	model = Book

	def get_queryset(self):
 		try:
 			return Book.on_site.filter(tag__code__exact=self.kwargs['slug'])
 		except Book.DoesNotExist:
 			raise Http404()

	def get_context_data(self, **kwargs):
		context = super(BookTagView, self).get_context_data(**kwargs)
		context.update({
			'tag_details': get_object_or_404(Tag, code=self.kwargs['slug']),
			})
		return context


class BookAuthorView(generic.ListView):
	model = Book

	def get_queryset(self):
		#return get_list_or_404(Book, tag__code__exact=self.kwargs['slug'])
 		try:
 			return Book.on_site.filter(author__code__exact=self.kwargs['slug'])
 		except Book.DoesNotExist:
 			raise Http404()

	def get_context_data(self, **kwargs):
		context = super(BookAuthorView, self).get_context_data(**kwargs)
		context.update({
			'author_details': get_object_or_404(Author, code=self.kwargs['slug']),
			})
		return context


def book_search(request):
	if request.method == 'GET':
		form = SearchForm(request.GET)

		if form.is_valid():
			get_form = form.cleaned_data['q']
			search_icontain = Book.on_site.all().filter(title__icontains=get_form)
			context = {'search_result': search_icontain, 'get_form': get_form}
			return render(request, 'book/book_search.html', context)

	return render(request, 'book/book_search.html')


def redirectshort(request, pk):
	book = get_object_or_404(Book, pk=pk)
	return redirect('book:book-detail', genre=book.genre, book=book.code)


def redirect_to_index(request):
	return redirect('index')