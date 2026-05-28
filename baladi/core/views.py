from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'titulo':'Bienvenido a mi sitio',
    } 
    return render(request, 'core/home.html', context)
