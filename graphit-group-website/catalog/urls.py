from django.http import Http404
from django.urls import path, include
from . import views

def trigger_404(request):
    raise Http404()

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/<int:catalog_id>/', views.catalog_detail, name='catalog_detail'),
    path('<slug:url>/', views.base_page, name='base_page'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('test-404/', trigger_404),
]