
from django import forms

class RegForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
   
