from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:pk>/', products, name='products_category')
]