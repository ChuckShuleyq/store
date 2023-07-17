from django.shortcuts import render
from product.models import Product, ProductCategory
from django.http import HttpRequest
# Create your views here.
def home(request: HttpRequest):
    context = {'title': "Store"}
    return render(request, 'product/index.html', context)
def products(request):
    context = {'title': "Store - Каталог", 'products': Product.objects.all(), 'categories': ProductCategory.objects.all()
    }
    return render(request, 'product/products.html', context)
