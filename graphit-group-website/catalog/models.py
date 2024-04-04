from django.db import models

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
