from django import forms 

class UpdateForm(forms.Form):
        def __init__(self, max_values = None, *args, **kwargs):
            super(UpdateForm, self).__init__(*args, **kwargs)
            ##print(kwargs)
            if max_values is not None:
                self.fields['quantity'] = forms.IntegerField(max_value=max_values['quantity'])
        id = forms.IntegerField(min_value = 0, widget = forms.HiddenInput)
        quantity = forms.IntegerField(min_value = 0)
        update = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)