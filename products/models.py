from django.db import models

class Category(models.Model):
    id_category = models.IntegerField()
    category = models.CharField(max_length=200)
    id_subcategory = models.IntegerField()
    subcategory = models.CharField(max_length=200)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    image_url = models.URLField(max_length=200)
    id_category = models.IntegerField(default=-1)
    id_subcategory = models.IntegerField(default=-1)