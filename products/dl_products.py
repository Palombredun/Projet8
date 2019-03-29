import json
import requests
import time

with open('category_tree.json', 'r') as f:
    category_tree = json.load(f)



base_link = "https://fr.openfoodfacts.org/categorie/"

def strip_useless_characters(string):
    return string.strip().replace('-', '')

def count_letters(string):
    string = strip_useless_characters(string)
    count = {}
    for letter in string:
        if letter in count.keys():
            count[letter] += 1
        else:
            count[letter] = 1
    return count

products = {}
# product organisation :
# {'category': 
#            {product_name: 
#                {
#                'nutriscore': nutriscore,
#                'url': image_url
#                }}}

compteur = 0
# explore 3 pages of products and extract their name, nutriscore and image url :
for page in range(1,4):
    for key in category_tree.keys():
        # explore the list of subcategories
        for category in category_tree[key].keys():
            for subcategory in category_tree[key][category]:
                print(compteur)
                time.sleep(1)
                link = base_link + subcategory + '/' + str(page) + '.json'
                resp = requests.get(link)
                req = resp.json()
                
                i = 0
                # extract the data needed for each product and add it to the dict product
                for _ in req['products']:
                    if subcategory not in products.keys():
                        products[subcategory] = {}
                    product_name = req['products'][i]['product_name']
                    if product_name not in products[subcategory].keys():
                        products[subcategory][product_name] = {}
                    
                    if ('image_front_url' in req['products'][i].keys() and
                        'nutrition_grade_fr' in req['products'][i].keys()):
                        products[subcategory][product_name]['image_url'] = \
                            req['products'][i]['image_front_url']
                        products[subcategory][product_name]['nutriscore'] = \
                            req['products'][i]['nutrition_grade_fr']
                    i += 1
                compteur += 1


with open('products_tree.json', 'w') as f:
    json.dump(products, f, indent=4)