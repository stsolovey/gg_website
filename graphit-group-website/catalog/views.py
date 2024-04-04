from django.shortcuts import render
from .models import ProductCatalog

def home(request):
    catalogs = ProductCatalog.objects.all()
    return render(request, 'catalog/index.html', {'catalogs': catalogs})
