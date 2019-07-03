from django.db import models

class Category(models.Model):
	category_name = models.CharField(max_length=200)

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	nutriscore = models.CharField(max_length=1)
	image_url = models.URLField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	purchase_places = models.CharField(max_length=100, null=True)
	energy_100g = models.FloatField(null=True)
	fat_100g = models.FloatField(null=True)
	saturated_fats_100g = models.FloatField(null=True)
	carbohydrates_100g = models.FloatField(null=True)
	sugars_100g = models.FloatField(null=True)
	fibers_100g = models.FloatField(null=True)
	proteins_100g = models.FloatField(null=True)
	salt_100g = models.FloatField(null=True)