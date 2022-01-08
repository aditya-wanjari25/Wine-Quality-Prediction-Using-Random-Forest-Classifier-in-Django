from django.forms import ModelForm
from .models import *
class UserForm(ModelForm):
    class Meta:
        model = UserInput    
        fields = '__all__' 