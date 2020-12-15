from django.db import models
import os

class Product(models.Model):
	name 			= models.CharField(max_length=50, unique=True)
	product_type 	= models.CharField(max_length=20)
	description		= models.CharField(max_length=5000, null=False, blank=True, default="")
	specifications	= models.CharField(max_length=2000, null=False, blank=True, default="")
	price 			= models.IntegerField(null=False)
	discount 		= models.IntegerField(default=0)
	pub_date 		= models.DateTimeField('date published')

	def __str__(self):
		return self.name

class Image(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='static/')
	def __str__(self):
		return self.image.name + " -> " + self.product.name 

class CampaignItem(models.Model):
	item = models.ManyToManyField(Product)