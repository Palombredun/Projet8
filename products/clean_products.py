import json
from difflib import SequenceMatcher
from itertools import islice

def check_product(prod, products_approved):
    """
    
    """
    if prod in products_approved:
        return True
    else:
        for product in products_approved:
            if SequenceMatcher(None, prod, product).ratio() > 0.8:
                return True


with open('products_tree.json', 'r') as f:
    data = json.load(f)

products_approved = []
cleaned_products = {}

for category in data.keys():
    for subcategory in data[category].keys():
        for i, prod in data[category][subcategory].items():
            # for each product, check if it has many similarities to the previous products
            # already added to the database.
            if check_product(prod, products_approved) is not True:
                del data[category][subcategory][prod]
            else:
                products_approved.append(prod)


with open('cleaned_products.json', 'w') as f:
    json.dump(data, f, indent=4)