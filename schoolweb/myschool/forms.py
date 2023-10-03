from django import forms
from .models import YourModel 

class RegForm(forms.ModelForm):
    class Meta:
        model = YourModel 
        fields = ['field1', 'field2', ...] 