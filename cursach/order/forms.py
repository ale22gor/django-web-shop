from django import forms 
from .models import Order


class OrderFormCreate(forms.ModelForm):
        
        class Meta:
                model = Order
                fields = ['city', 'street', 'house', 'flat']