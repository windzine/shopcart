from django.shortcuts import render
from .models import Product, Cart


def index_product(request):
    product_list = Product.objects.all()
    return render(request, 'index_product.html', {'product_list': product_list})


def index_cart(request):
    cart_list = Cart.objects.filter(customer=request.user)
    return render(request, 'cart.html', {'cart_list': cart_list})
