from .models import Section

def getContext():
	sections = Section.objects.order_by('name')

	context = {}
	if len(sections) > 0:
		context = {
			"sections": sections
		}
	
	return context;