from bs4 import BeautifulSoup
import requests
import json

base_url = "https://fr.openfoodfacts.org/categorie/"
categories = [
    'aliments-d-origine-vegetale',
    'snacks',
    'boissons',
    'snacks-sucres',
    'produits-laitiers',
    'plats prepares',
    'boissons-sans-alcool',
    'viandes',
    'aliments-a-base-de-fruits-et-legumes',
    'produits-fermentes',
    'produits-laitiers-fermentes',
    'cereales-et-pomme-de-terre',
    'produits-a-tartiner',
    'biscuits-et-gateaux',
    'petits-dejeuners',
    'fromages',
    'charcuteries',
    'epicerie',
    'desserts',
    'fruits-et-produits-derives'
    ]

id_cat = 0
id_sub = 0
category_tree = []
for category in categories:
    url = base_url + category
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    croutons = soup.find_all(class_="tag_well_known")

    for link in soup.findAll('a', {'class': 'tag well_known'}):
        try:
            category_tree.append({'id_category': id_cat, 
                'category_name': category, 
                'id_subcategory': id_sub, 
                'subcategory_name': str(link['href'].replace("/categorie/", ""))})
            id_sub += 1
        except KeyError:
            pass
    id_cat += 1
with open('category_tree.json', 'w') as f:
    json.dump(category_tree, f, indent=4)