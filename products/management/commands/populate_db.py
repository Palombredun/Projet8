import json

from django.core.management.base import BaseCommand, CommandError
from products.models import Product

class Command(BaseCommand):
    help = "Populate the database with the products previously downloaded."

    def handle(self, *args, **options):
        with open("products/create_db/cleaned_products.json", 'r') as f:
            data = json.load(f)

        for elt in data:
            new_product = Product(
                product_name=elt['product_name'],
                nutriscore=elt['nutriscore'],
                image_url=elt['image_url'],
                id_category=elt['id_category'],
                id_subcategory=elt['id_subcategory']
                )
            new_product.save()