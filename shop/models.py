from django.db import models

from enum import Enum

class ProductType(Enum):
	BEAUTY =1
	ECOCLOTHES =2

class Product(models.Model):
	name 			= models.CharField(max_length=50, unique=True)
	product_type 	= models.CharField(max_length=20)
	image_link 		= models.CharField(max_length=200)
	price 			= models.IntegerField(null=False)
	discount 		= models.IntegerField(default=0)
	pub_date 		= models.DateTimeField('date published')