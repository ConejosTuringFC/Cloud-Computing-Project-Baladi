from django.shortcuts import render
from django.http  import HttpResponse
from .models import Flux
from datetime import datetime

# Create your views here.

def index(request):
	now = datetime.now()
	flux = Flux(now, 1.0)
	flux.save()
	return HttpsResponse("Este es mi microservicio")
