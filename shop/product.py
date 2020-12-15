from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.conf import settings

from .models import Product
from .models import Image

def main(request, section, product):
	product = Product.objects.filter(product_type=section, id=product)[:1]
	template = loader.get_template('product.html')
	imgs = Image.objects.filter(product=product[0])

	specifications = None
	if len(product[0].specifications) > 0:
		specifications = product[0].specifications.split(",")


	context = {
		"product": product[0],
		"section": section,
		"specifications": specifications,
		"currency": settings.CURRENCY,
		"imgs": imgs
	}

	return HttpResponse(template.render(context, request))