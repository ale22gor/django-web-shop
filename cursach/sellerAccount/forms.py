from django import forms 
from order.models import Order
from products.models import Product


class OrderEditForm(forms.ModelForm):
        
        class Meta:
                model = Order
                fields = ['paid']
                
class ProductEditForm(forms.ModelForm):
        
        class Meta:
                model = Product
                fields = ['Amount']

