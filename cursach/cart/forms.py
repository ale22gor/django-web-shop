from django import forms 

class UpdateForm(forms.Form):
        id = forms.IntegerField(min_value = 0, widget = forms.HiddenInput)
        quantity = forms.IntegerField(min_value = 0)
        update = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)