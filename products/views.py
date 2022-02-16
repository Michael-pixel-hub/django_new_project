from django.shortcuts import render
import json
from django.conf import settings
from products.models import Product

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all()
    }

    return render(request, "products/products.html", context)
