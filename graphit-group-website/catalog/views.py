from django.shortcuts import render, get_object_or_404
from .models import ProductCatalog, BasePage

def home(request):
    category_id = request.GET.get('category', 'all')
    manufacturer_id = request.GET.get('manufacturer', 'all')

    catalogs = ProductCatalog.objects.all()

    if category_id != 'all':
        catalogs = catalogs.filter(categories__id=category_id)

    if manufacturer_id != 'all':
        catalogs = catalogs.filter(manufacturer__id=manufacturer_id)

    return render(request, 'catalog/index.html', {'catalogs': catalogs})

def catalog_detail(request, catalog_id):
    catalog = get_object_or_404(ProductCatalog, id=catalog_id)
    return render(request, 'catalog/catalog_detail.html', {'catalog': catalog})

def base_page(request, url):
    page = get_object_or_404(BasePage, url=url)
    return render(request, 'base_page.html', {'page': page})