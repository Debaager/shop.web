from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        qs = super().get_queryset()
        cat = self.request.query_params.get('category')
        sort = self.request.query_params.get('sort', 'name')
        if cat: qs = qs.filter(category=cat)
        return qs.order_by(sort)
