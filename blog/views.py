from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from markdownx.utils import markdownify

# Create your views here.
from .models import Post


def blog_all(request):
	blog_list = Post.objects.all()
	context = {'blog_list': blog_list}

	#return HttpResponse(markdownify(blog_list[0].body))
	return render(request, 'body.html', context)

class PostDetailView(generic.DetailView):
	model = Post

	def get_object(self):
 		try:
 			return Post.objects.get(code=self.kwargs['slug'])
 		except Post.DoesNotExist:
 			raise Http404()