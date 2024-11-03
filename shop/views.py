from django.shortcuts import render
from shop.models import Product

def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})

def orders(request):
    return render(request, 'shop/orders.html')

def create_order(request):
    return render(request, 'shop/create_order.html')

def product_detail(request):
    return render(request, 'shop/product_detail.html')
