from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import OrderFormCreate, AdressCreateForm
from cart.cart import Cart
from .models import OrderItem
from products.models import Product


# Create your views here.

def create_address(request):
    if request.POST:
            form = AdressCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                return render(request, 'Order/created.html' ,{'form': form})
    form = AdressCreateForm()
    return render(request,'Order/created.html',{ 'form': form})

def create_order(request):
    cart = Cart(request)
    if request.POST:
            form = OrderFormCreate(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    ##not safe chnge to get product by id
                    OrderItem.objects.create(order = order, product = Product.objects.get(id = item['id']), quantity = item['quantity'])

                print(order.get_total_cost())
                cart.clear()
                print('a')
                return redirect('order:address')
    form = OrderFormCreate()
    return render(request,'Order/home.html',{ 'cart':cart, 'form': form})

