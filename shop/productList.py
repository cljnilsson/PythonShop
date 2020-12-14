from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product
from mainsite.core import getContext

# Create your views here.

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def main(request, section):
	products = Product.objects.filter(product_type=section).order_by('name')
	template = loader.get_template('productList.html')

	ordered = split(products, 4)
	context = {}
	if len(products) > 0:
		context = {
			'products': ordered,
			"section": section
		}

	context.update(getContext())
	
	return HttpResponse(template.render(context, request))