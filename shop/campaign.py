from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.conf import settings

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
	products = CampaignItem.objects.all()
	template = loader.get_template('productList.html')

	ordered = split(products[0].item.all(), 3)
	context = {}
	if len(products) > 0:
		context = {
				'products': ordered,
				"currency": settings.CURRENCY
			}

	context.update(getContext())
	
	return HttpResponse(template.render(context, request))	