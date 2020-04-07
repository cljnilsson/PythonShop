from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product

def main(request, section, product):
	product = Product.objects.filter(product_type=section, id=product)[:1]
	template = loader.get_template('product.html')

	context = {
		"product": product[0],
		"section": section
	}

	return HttpResponse(template.render(context, request))