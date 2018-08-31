from django.urls import path, re_path
from . import views
from flatpages import views as flatpages_view
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

app_name="blog"

urlpatterns = [
	path('', views.blog_all, name='blog-all'),
	path('/<slug>', views.PostDetailView.as_view(), name='post'),
]