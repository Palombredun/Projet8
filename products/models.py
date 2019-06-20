from django.db import models

class Category(models.Model):
	category_name = models.CharField(max_length=200)

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	nutriscore = models.CharField(max_length=1)
	image_url = models.URLField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	purchase_places = models.CharField(max_length=50)
	calories_100g = models.FloatField()
	acides_gras_saturees_100g = models.FloatField()
	glucides_100g = models.FloatField()
	sucres_100g = models.FloatField()
	fibres_100g = models.FloatField()
	proteines_100g = models.FloatField()
	sel_100g = models.FloatField()