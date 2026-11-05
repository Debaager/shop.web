from urllib.parse import unquote

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import transaction
from catalog.models import Product
from .models import Order, OrderItem

@require_POST
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    return JsonResponse({'count': sum(cart.values())})

def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        p = Product.objects.get(id=pid)
        sub = p.price * qty
        total += sub
        items.append({'product': p, 'quantity': qty, 'subtotal': sub})
    return render(request, 'cart/detail.html', {'items': items, 'total': total})

@require_POST
def update_qty(request, product_id):
    qty = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    key = str(product_id)
    if qty <= 0: cart.pop(key, None)
    else: cart[key] = qty
    request.session['cart'] = cart
    return JsonResponse({'ok': True})

@require_POST
def remove_item(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return JsonResponse({'ok': True})

@require_POST
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart: return redirect('cart')
    with transaction.atomic():
        order = Order(city=unquote(request.COOKIES.get('city', '—')), total=0)
        order.save()
        total = 0
        for pid, qty in cart.items():
            p = Product.objects.get(id=pid)
            OrderItem.objects.create(order=order, product=p, quantity=qty, price=p.price)
            total += p.price * qty
        order.total = total
        order.save()
    request.session['cart'] = {}
    return redirect('cart')
