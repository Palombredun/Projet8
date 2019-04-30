import json

from django.core.management.base import BaseCommand, CommandError
from products.models import Category

class Command(BaseCommand):
    help = 'Populate the DB with the category tree previously created.'

    def handle(self, *args, **options):
        with open("products/create_db/category_tree.json", "r") as f:
            data = json.load(f)

        for elt in data:
            new_sub_cat = Category(
                id_category=elt['id_category'],
                category=elt['category_name'],
                id_subcategory=str(elt['id_subcategory']),
                subcategory=elt['subcategory_name']
                )
            new_sub_cat.save()