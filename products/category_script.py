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

index = 0
category_tree = {}
for categorie in categories:
    # for each category, get the page containing its subcategories
    if index not in category_tree.keys():
        category_tree[index] = {categorie: []}

    url = base_url + categorie
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    croutons = soup.find_all(class_='tag well_known')
    croutons = list(croutons)
    # extract subcategories
    for crouton in croutons:
        crouton = str(crouton)
        crouton = crouton.split(' ')
        for crouty in crouton:
            if 'href' in crouty:
                crouton = crouty
                break
        crouton = crouton.split('"')[1]
        crouton = crouton.replace('/categorie/', '')
        category_tree[index][categorie].append(crouton)
    index += 1
with open('category_tree.json', 'w') as f:
    json.dump(category_tree, f, indent=4)