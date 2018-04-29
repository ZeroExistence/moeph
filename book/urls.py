from django.urls import path
from . import views
from flatpages import views as flatpages_view
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

app_name="book"

urlpatterns = [
	path('', flatpages_view.index, name='index'),
	path('all', views.book_all, name='book-all'),
	path('tag/<slug>', views.BookTagView.as_view(), name='book-tag'),
	path('author/<slug>', views.BookAuthorView.as_view(), name='book-author'),
	path('search', views.book_search, name='book-search'),
	path('<slug>/', views.BookListView.as_view(), name='book'),
	path('<slug:genre>/<slug:book>', views.BookDetailView.as_view(), name='book-detail'),
	path('<pk>', views.redirectshort, name='redirectshort'),
]