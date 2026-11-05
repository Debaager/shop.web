from django.core.management.base import BaseCommand
from catalog.models import Product
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not Product.objects.exists():
            Product.objects.create(name='Ноутбук', price=50000, category='Электроника')
            Product.objects.create(name='Мышь', price=1500, category='Электроника')
            Product.objects.create(name='Книга', price=800, category='Книги')
            self.stdout.write('Товары добавлены')
