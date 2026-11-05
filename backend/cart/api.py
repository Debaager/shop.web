from rest_framework.views import APIView
from rest_framework.response import Response
from catalog.models import Product
class CartView(APIView):
    def get(self, request):
        cart = request.session.get('cart', {})
        items = []
        total = 0
        for pid, qty in cart.items():
            p = Product.objects.get(id=pid)
            sub = float(p.price) * qty
            total += sub
            items.append({'id': p.id, 'name': p.name, 'price': float(p.price), 'quantity': qty, 'subtotal': sub})
        return Response({'items': items, 'total': total})
    def post(self, request, product_id=None):
        cart = request.session.get('cart', {})
        key = str(product_id)
        cart[key] = cart.get(key, 0) + 1
        request.session['cart'] = cart
        return Response({'count': sum(cart.values())})
    def delete(self, request, product_id):
        cart = request.session.get('cart', {})
        cart.pop(str(product_id), None)
        request.session['cart'] = cart
        return Response({'count': sum(cart.values())})
