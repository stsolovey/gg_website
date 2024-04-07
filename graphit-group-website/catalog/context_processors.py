from .models import Category, Manufacturer, BasePage

def categories_and_manufacturers(request):
    return {
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
    }

def base_pages(request):
    pages = BasePage.objects.all()
    return {'base_pages': pages}
