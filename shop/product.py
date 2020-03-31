from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product

def main(request, section, product):
	products = Product.objects.filter(product_type=section, name=product)[:1]
	template = loader.get_template('product.html')
	context = {}
	
	return HttpResponse(template.render(context, request))