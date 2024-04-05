from django.shortcuts import render, get_object_or_404
from .models import ProductCatalog

def home(request):
    catalogs = ProductCatalog.objects.all()
    return render(request, 'catalog/index.html', {'catalogs': catalogs})


def catalog_detail(request, catalog_id):
    catalog = get_object_or_404(ProductCatalog, id=catalog_id)
    return render(request, 'catalog/catalog_detail.html', {'catalog': catalog})