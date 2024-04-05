from .models import Category, Manufacturer

def categories_and_manufacturers(request):
    return {
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
    }