import json
from difflib import SequenceMatcher

def is_duplicate(prod_name, products_approved):
    """
    
    """
    if prod_name in products_approved:
        return True
    else:
        for product in products_approved:
            if SequenceMatcher(None, prod_name, product).ratio() > 0.6:
                return True

def clean_products():
    """
    take the products tree and for each subcategory return
    a maximum of 30 products in another json file    
    """
    with open('products_tree.json', 'r') as f:
        data = json.load(f)

    # for each product, check if it's not already in the list
    # if not, add it and its characteristics to 'cleaned_products'
    # add in a list the ids of th subcategories added
    products_approved = []
    cleaned_products = []
    j = 0
    cat = []
    for i, elt in enumerate(data):
        if is_duplicate(elt['product_name'], products_approved) is not True:
            cleaned_products.append({
                'id_product': elt['id_product'],
                'product_name': elt['product_name'],
                'nutriscore': elt['nutriscore'],
                'image_url': elt['image_url'],
                'id_category': elt['id_category'] ,
                'id_subcategory': elt['id_subcategory']
                })
            j += 1
            if elt['id_subcategory'] not in cat:
                cat.append(elt['id_subcategory'])

    #for each subcategory, add the 25 first products to the nested list tmp
    tmp = []
    for i in cat:
        tmp.append([item for item in cleaned_products if \
            item['id_subcategory'] == i][:25])
    
    # 'un-nest' tmp
    products = []
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            products.append(tmp[i][j])

    with open('cleaned_products.json', 'w') as f:
        json.dump(products, f, indent=4)

if __name__ == '__main__':
    clean_products()