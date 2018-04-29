from flatpages import views
from django.urls import path

app_name="flatpages"

urlpatterns = [
    path('<path:url>', views.flatpage, name='flatpage'),
]
