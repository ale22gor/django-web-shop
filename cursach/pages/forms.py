from django import forms 
from django.contrib.auth import  get_user_model
User = get_user_model()

class RegisterForm(forms.Form):
        username = forms.CharField()
        email = forms.CharField()
        password = forms.CharField(widget = forms.PasswordInput)
        password2 = forms.CharField(label = 'Confirm password', widget = forms.PasswordInput)
        
        def clean_username(self):
            username = self.cleaned_data.get("username")
            qs = User.objects.filter(username = username)
            if qs.exists():
                raise forms.ValidationError("Username is already taken")
            return username
        
        def clean(self):
            data = self.cleaned_data
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('password2')
            if password2 != password:
                raise forms.ValidationError("Password must much")
            return data 