from difflib import SequenceMatcher

from django.shortcuts import render


def search(request):
    pass
    #if 'query' in request.GET:
    #    query =  request.GET['query']
    #    products = Product.objects.filter(product_name__icontains=query)
    #    if products.count() == 0:
    #        return render(request, 'ersatz/result.html')
    #    else:
    #        # create a list of tuples with the product and its ratio
    #        # compared to the search of the user, the product with the best
    #        # ratio will be chosen
    #        scores = []
    #        for product in products:
    #            scores.append((
    #                product, 
    #                SequenceMatcher(None, query, product.product_name).ratio())
    #                )
    #        scores.sort(key=lambda x: x[1])
    #        
    #        product_to_replace = scores[-1][0]
    #        
    #        simili_products = Product.objects.filter(
    #            id_category=product_to_replace.id_category
    #            ).order_by('nutriscore')
    #        
    #        ersatz = []
    #        for prod in simili_products:
    #            if prod.nutriscore < product_to_replace.nutriscore:
    #                ersatz.append(prod)
    #                
    #        # return only the top 6 of the products
    #        return render(request, 'ersatz/result.html', {'products': ersatz[:6]})