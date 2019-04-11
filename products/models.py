from django.db import models

class Prodcut(models.Model):
	id_product = models.IntegerField()
	product_name = models.CharField(max_length=100)
	nutriscore = models.CharField(max_length=1)
	image_url = models.URLField(max_length=200)
	id_category = models.IntegerField()
	id_subcategory = models.IntegerField()
