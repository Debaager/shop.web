from urllib.parse import unquote

def cities(request):
    from .views import CITIES
    current_city = request.COOKIES.get('city')
    if current_city:
        current_city = unquote(current_city) # Декодируем для шаблона
    return {
        'cities': CITIES,
        'current_city': current_city, # Передаем в шаблон
    }

def cart_count(request):
    cart = request.session.get('cart', {})
    return {'cart_count': sum(cart.values())}