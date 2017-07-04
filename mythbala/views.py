from django.shortcuts import get_object_or_404, render

from .models import Week, Thing


# Create your views here.
def index(request):
	# in the future, add possibility to view current time here?
	weeks = Week.objects.all()
	context = {
		'weeks' : weeks
	}
	return render(request, 'mythbala/index.html', context)

def week_detail(request, week_number):
	week = get_object_or_404(Week, pk=week_number)
	return render(request, 'mythbala/week_detail.html',
		{'week': week})

def thing_detail(request, week_number, thing_name):
	thing = get_object_or_404(Thing, pk=thing_name)
	return render(request, 'mythbala/thing_detail.html',
		{'thing': thing,
		'week_number': week_number})
