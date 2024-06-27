from django.shortcuts import redirect, render
from shop.models import Product
from .models import Cart

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Cart.objects.create(product=product, quantity=1)
    return redirect('cart_detail')

def cart_detail(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart/detail.html', {'cart_items': cart_items})
