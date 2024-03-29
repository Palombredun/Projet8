from django.db import models
from django.contrib.auth.models import User

from products.models import Product

class Favourite(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product)