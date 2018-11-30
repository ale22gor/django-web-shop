from django import forms 
from .models import Order


class OrderFormCreate(forms.ModelForm):
        
        class Meta:
                model = Order
                fields = ['first_name','last_name','email','city', 'street', 'house', 'flat']