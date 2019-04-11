import json

with open('_products_tree.json', 'r') as f:
    data = json.load(f)

data_copy = data[:]

cat = {}
compteur = 0
for i, elt in enumerate(data_copy):
    if elt['id_subcategory'] not in cat.keys():
        cat[elt['id_subcategory']] = 1
        compteur += 1
    else:
        cat[elt['id_subcategory']] += 1

cp = []
for i in range(compteur):
    cp.append([item for item in data if item['id_subcategory'] == 0][:25])

products = []
for i in range(len(cp)):
    for j in range(len(cp[i])):
        products.append(cp[i][j])

print(len(products))

with open('cleaned_products.json', 'w') as f:
    json.dump(products, f, indent=4)