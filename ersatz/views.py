from django.shortcuts import render

from products.models import Product

#tata = Product.objects.filter(product_name__icontains="coca", id_subcategory=46)
def search(request):
	pass
	#if 'q' in request.GET:
	#	message = "You searched for : %r" % request.GET['q']
	#else:
	#	message = "You submitted and empty form"
	#return render(request, {'message': message})