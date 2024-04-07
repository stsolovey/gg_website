from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    image = models.ImageField(upload_to='categories/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    image = models.ImageField(upload_to='manufacturers/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductCatalog(models.Model):
    image = models.ImageField(upload_to='catalogs/')
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='catalogs/pdfs/')

    def __str__(self):
        return self.name

class BasePage(models.Model):
    title = models.CharField(max_length=200)
    body = CKEditor5Field('Content', config_name='default')
    url = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
