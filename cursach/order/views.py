from django.shortcuts import render
from django.views import generic
from cart.models import Cart, Entry
from .forms import OrderFormCreate
from django.contrib.auth import  get_user_model

User = get_user_model()

# Create your views here.
from django.contrib.auth import  get_user_model

def create_order(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)    
    if request.POST:
        form = OrderFormCreate(request.POST)
        if form.is_valid():
            order = form.save
            
            for x in cart_obj_current_entries:
                x.delete()
            return render(request,'Order/created.html')
    else:
        form = OrderFormCreate()
    return render(request,'Order/home.html',{ 'form': form, 'user': User})