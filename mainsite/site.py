from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.conf import settings

from shop.models import Product
from shop.models import Image
from .core import getContext



def main(request):
	template = loader.get_template('front.html')

	context = {
		"currency": settings.CURRENCY
	}

	context.update(getContext())

	# this is inefficient, make into a single query in the future
	
	for i, s in enumerate(context["sections"]):
		toadd = Product.objects.filter(product_type=s.name)[:4]
		for j, p in enumerate(toadd):
			img = Image.objects.filter(product=p)[:1]
			if(len(img) > 0):
				toadd[j].image = img[0].image
				#p.image = img[0].image

		setattr(context["sections"][i], "products", toadd)

	return HttpResponse(template.render(context, request))