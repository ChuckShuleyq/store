from django.shortcuts import render, HttpResponseRedirect
from product.models import Product, ProductCategory, Basket
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def home(request: HttpRequest):
    context = {'title': "Store"}
    return render(request, 'product/index.html', context)

def products(request, category_id=None, page_number=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all() 
    paginator = Paginator(product, 3)

    products_paginator = paginator.page(page_number)
    products_paginator.paginator.page_range
    context = {'title': "Store - Каталог", 'products': products_paginator, 'categories': ProductCategory.objects.all()}

    return render(request, 'product/products.html', context)

@login_required
def basket_add(request: HttpRequest, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER']) 

@login_required
def basket_remove(request: HttpRequest, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
