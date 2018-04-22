from django.urls import path
from . import views

# Create your views here.

app_name="page"

urlpatterns = [
	path('', views.index, name='home'),
	path('<slug:link>', views.PageView.as_view(), name='page'),
]