from django.forms import ModelForm
from .models import Myuser

class MyUserForm(ModelForm):
    class Meta:
        model = Myuser
        fields = ['name', 'last_name', 'age', 'country']