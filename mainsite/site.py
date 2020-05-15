from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Section
from .core import getContext

def main(request):
	template = loader.get_template('front.html')

	context = {
	}

	context.update(getContext())

	return HttpResponse(template.render(context, request))