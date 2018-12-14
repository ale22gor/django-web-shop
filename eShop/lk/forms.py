from django import forms 
from django.contrib.auth.models import  User
from order.models import Order

class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget = forms.PasswordInput)

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
        def clean_email(self):
                email = self.cleaned_data.get("email")
                qs = User.objects.filter(email = email)
                if qs.exists():
                        raise forms.ValidationError("Email is already taken")
                return email
        
        def clean_password2(self):
                cd = self.cleaned_data
                if cd['password'] != cd['password2']:
                        raise forms.ValidationError('Passwords dont match')
                return cd['password2']

class UserEditForm(forms.ModelForm):
    
    class Meta:
                
                model = User
                fields = ['first_name', 'last_name', 'email']
        
class OrderEdit(forms.ModelForm):
        class Meta:
                model = Order
                fields = ['paid']
           