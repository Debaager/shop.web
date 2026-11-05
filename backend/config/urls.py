from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.api import ProductViewSet
from cart.api import CartView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include(router.urls)),
    path('api/cart/', CartView.as_view()),
    path('api/cart/<int:product_id>/', CartView.as_view()),
]
