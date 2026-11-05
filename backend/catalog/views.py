from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Product
def product_list(request):
    qs = Product.objects.all()
    category = request.GET.get('category')
    if category: qs = qs.filter(category=category)
    sort = request.GET.get('sort', 'name')
    if sort in {'name','-name','price','-price'}: qs = qs.order_by(sort)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('catalog/_product_grid.html', {'products': qs}, request=request)
        return JsonResponse({'html': html})
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'catalog/list.html', {'products': qs, 'categories': categories})
