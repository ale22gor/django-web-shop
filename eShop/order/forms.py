from django import forms 
from .models import Order, Adress


class OrderFormCreate(forms.ModelForm):
        
        class Meta:
                model = Order
                fields = ['first_name','last_name','email']
class AdressCreateForm(forms.ModelForm):
        class Meta:
                model = Adress
                fields = ['city', 'street', 'house', 'flat']