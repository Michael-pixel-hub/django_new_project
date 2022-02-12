from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=25, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)