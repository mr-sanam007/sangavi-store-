from django.shortcuts import render
from .models import Product

# Create your views here.

def cart_view(request):
    return render(request, 'marketplace/cart.html')

def wishlist_view(request):
    return render(request, 'marketplace/wishlist.html')

def store_view(request):
    products = Product.objects.all()
    return render(request, 'marketplace/store.html', {'products': products})
