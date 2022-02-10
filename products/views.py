from django.shortcuts import render
import json


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, "products/index.html", context)


def products(request):
    with open('/home/michael/project_django/geekshop-server/geekshop/products/fixtures/products.json', 'r') as file:
        context = json.load(file)
    return render(request, "products/products.html", context)
