from django import forms 

class UpdateForm(forms.Form):
        quantity = forms.IntegerField(min_value = 0)