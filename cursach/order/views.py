from django.shortcuts import render
from django.views import generic
from .forms import OrderFormCreate
from cart.cart import Cart
from .models import OrderItem


# Create your views here.
from django.contrib.auth import  get_user_model

def create_order(request):
    cart = Cart(request)
    if request.POST:
            form = OrderFormCreate(request)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(product = item['name'], price = item['price'], quntity = item['quantity'])
                    cart.clear()
                    return render(request, 'Order/created.html' ,{'order':order})
    form = OrderFormCreate()
    return render(request,'Order/home.html',{ 'form': form, 'user': User})