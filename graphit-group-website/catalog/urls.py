from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/<int:catalog_id>/', views.catalog_detail, name='catalog_detail'),
    path('<slug:url>/', views.base_page, name='base_page'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
