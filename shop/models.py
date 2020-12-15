from django.db import models

class Product(models.Model):
	name 			= models.CharField(max_length=50, unique=True)
	product_type 	= models.CharField(max_length=20)
	description		= models.CharField(max_length=5000, null=False, blank=True, default="")
	specifications	= models.CharField(max_length=2000, null=False, blank=True, default="")
	image_link 		= models.CharField(max_length=200)
	price 			= models.IntegerField(null=False)
	discount 		= models.IntegerField(default=0)
	pub_date 		= models.DateTimeField('date published')

	def __str__(self):
		return self.name


class CampaignItem(models.Model):
	item = models.ManyToManyField(Product)