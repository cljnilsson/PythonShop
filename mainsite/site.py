from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def main(request):
	template = loader.get_template('front.html')

	context = {
	}

	return HttpResponse(template.render(context, request))