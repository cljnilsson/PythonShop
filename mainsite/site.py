from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from shop.models import Product
from .core import getContext

def main(request):
	template = loader.get_template('front.html')

	context = {
	}

	context.update(getContext())

	# this is inefficient, make into a single query in the future
	
	for i, s in enumerate(context["sections"]):
		toadd = Product.objects.filter(product_type=s.name)[:4]
		setattr(context["sections"][i], "products", toadd)

	return HttpResponse(template.render(context, request))