from django.db import models

class Prodcut(models.Model):
	product_name = models.CharField(max_length=100)
	nutriscore = models.CharField(max_length=1)
	photo_url = models.URLField(max_length=200)
	category = models.IntegerField()
