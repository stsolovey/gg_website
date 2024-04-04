from django import forms
from django.contrib import admin
from .models import Category, Manufacturer, ProductCatalog

class ProductCatalogForm(forms.ModelForm):
    class Meta:
        model = ProductCatalog
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

class ProductCatalogAdmin(admin.ModelAdmin):
    form = ProductCatalogForm

admin.site.register(ProductCatalog, ProductCatalogAdmin)
admin.site.register(Category)
admin.site.register(Manufacturer)
