import json
import requests
import time

def download_products():
    with open('category_tree.json', 'r') as f:
        category_tree = json.load(f)
    
    base_link = "https://fr.openfoodfacts.org/categorie/"    

    counter = 0
    products = [{}]
    # explore 15 pages of products and extract their name, nutriscore and image url
    for page in range(1,15):
        for i, elt in enumerate(category_tree):
            print(counter)
            link = base_link + \
                elt['subcategory_name'] + \
                '/' + \
                str(page) + '.json'
            resp = requests.get(link)
            req = resp.json()

            j = 0 
            for _ in req['products']:
                if 'product_name' in req['products'][j].keys() and \
                    'image_front_url' in req['products'][j].keys() and \
                    'nutrition_grade_fr' in req['products'][j].keys():

                    products.append({
                        'product_name': req['products'][j]['product_name'],
                        'nutriscore': req['products'][j]['nutrition_grade_fr'],
                        'image_url': req['products'][j]['image_front_url'],
                        'id_category': elt['id_category'],
                        'category_name': elt['category_name'],
                        'id_subcategory': elt['id_subcategory'],
                        'subcategory_name': elt['subcategory_name']
                        })
                j += 1
            counter += 1
    
    with open('products_tree.json', 'w') as f:
        json.dump(products, f, indent=4)

if __name__ == '__main__':
    download_products()