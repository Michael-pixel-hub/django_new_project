from django.shortcuts import render
import json
from django.conf import settings
from products.models import Product, ProductCategory

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'products_category': ProductCategory.objects.all()
    }

    return render(request, "products/products.html", context)
