from django import forms 
from django.contrib.auth.models import  User

class BuyForm(forms.Form):
        quantity = forms.IntegerField()
       