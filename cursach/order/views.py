from django.shortcuts import render
from django.views import generic
from .forms import OrderFormCreate
from cart.cart import Cart
from .models import OrderItem
from products.models import Product


# Create your views here.
from django.contrib.auth import  get_user_model

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
                return render(request, 'Order/created.html' ,{'order': order, 'order_total':order.get_total_cost()})
    form = OrderFormCreate()
    return render(request,'Order/home.html',{ 'cart':cart, 'form': form})