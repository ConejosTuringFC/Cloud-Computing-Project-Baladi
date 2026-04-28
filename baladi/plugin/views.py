from django.shortcuts import render
from django.http  import HttpResponse
from .models import Flux
from datetime import datetime

# Create your views here.

def index(request):
	data = Flux.objects.values()
	now = datetime.now()
	flux = Flux(date_time=now, flux=1.0)
	flux.save()
	data = list(Flux.objects.values())
	import json
	data = json.dumps(data, default=str)
	return HttpResponse(data, content_type = 'application/json')
