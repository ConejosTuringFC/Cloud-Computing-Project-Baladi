from django.shortcuts import render
from django.http  import HttpResponse
from .models import Flux, Myuser
from .forms import MyUserForm
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
	data = Flux.objects.values()
	now = datetime.now()
	flux = Flux(date_time=now, flux=1.0, name="hello")
	flux.save()
	data = list(Flux.objects.values())
	import json
	data = json.dumps(data, default=str)
	return HttpResponse(data, content_type = 'application/json')

class Myuserview(View):
    form_class = MyUserForm
    template_name = "plugin/info.html"
    initial = {'key': 'value'}
    
    def get(self, request,*args, **kwargs):
        # id_key = self.kwargs['id_key']
        id_key = self.kwargs.get('id_key')
        
        try:
            data = Myuser.objects.get(id=id_key)
            form = self.form_class(instance=data)   
            
        except Myuser.DoesNotExist:
            form = self.form_class(initial=self.initial)
            id_key = 0
            
        return render(request, self.template_name, {'form': form, 'id_key': id_key})
            
    
    # @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Myuserview, self).dispatch(*args, **kwargs)
	
    # return HttpResponse(data, content_type = 'application/json')