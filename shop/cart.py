from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import json

from .models import CampaignItem
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

def main(request):
	cart = json.loads(request.COOKIES.get("cart"))
	print(type(cart))
	products = CampaignItem.objects.all()
	template = loader.get_template('cart.html')

	# ordered = split(cart, 3)
	context = {}
	if len(products) > 0:
		context = {
				'cart': cart	
			}

	context.update(getContext())
	
	return HttpResponse(template.render(context, request))