import json
from os import name

from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product

def load_from_json(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.object.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)
        
        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            category_item = Product.objects.get(name = category_name)
            product['category'] = category_item
            Product.objects.create(**product)
