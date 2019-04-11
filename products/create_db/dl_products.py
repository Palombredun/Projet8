import json
import requests
import time

def download_products():
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
    

    counter = 0
    id_product = 0
    products = [{}]
    # explore 15 pages of products and extract their name, nutriscore and image url
    for page in range(1,15):
        for i, elt in enumerate(category_tree):
            print(counter)
            link = base_link + elt['subcategory'] + '/' + \
                    str(page) + '.json'
            resp = requests.get(link)
            req = resp.json()

            j = 0 
            for _ in req['products']:
                if 'product_name' in req['products'][j].keys() and \
                    'image_front_url' in req['products'][j].keys() and \
                    'nutrition_grade_fr' in req['products'][j].keys():
                    products.append({
                        'id_product': id_product,
                        'product_name': req['products'][j]['product_name'],
                        'nutriscore': req['products'][j]['nutrition_grade_fr'],
                        'image_url': req['products'][j]['image_front_url'],
                        'id_subcategory': elt['id_subcategory'],
                        'id_category': elt['id_category']
                        })
                    id_product += 1
                j += 1
            counter += 1
    
    with open('products_tree.json', 'w') as f:
        json.dump(products, f, indent=4)

if __name__ == '__main__':
    download_products()