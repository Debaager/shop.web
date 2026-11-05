from django.shortcuts import redirect, render
CITIES = ['Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск']
def home(request): return render(request, 'shop/home.html')
from urllib.parse import quote, unquote

def set_city(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        resp = redirect(request.POST.get('next', '/'))
        if city in CITIES:
            # Кодируем кириллицу перед записью в cookie
            resp.set_cookie('city', quote(city), max_age=365*24*3600)
        return resp
    return render(request, 'shop/choose_city.html', {'cities': CITIES})