from django.urls import path
from . import views
from page import views as page_view

app_name="book"

urlpatterns = [
	path('', page_view.index, name='index'),
	path('all', views.book_all, name='book-all'),
	path('tag/<slug>', views.BookTagView.as_view(), name='book-tag'),
	path('author/<slug>', views.BookAuthorView.as_view(), name='book-author'),
	path('search', views.book_search, name='book-search'),
	path('<slug>/', views.BookListView.as_view(), name='book'),
	#path('<slug:pk>/', views.GenreDetailView.as_view(), name='genre'),
	#path('<slug:genre>/<slug:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('<slug:genre>/<slug:book>', views.BookDetailView.as_view(), name='book-detail'),
]