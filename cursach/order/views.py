from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import OrderFormCreate, AdressCreateForm
from cart.cart import Cart
from .models import OrderItem
from products.models import Product


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.POST:
            order_form = OrderFormCreate(request.POST)
            address_form = AdressCreateForm(request.POST)
            if order_form.is_valid():
                order = order_form.save()
                if address_form.is_valid():
                    EmptyFields = False
                    if None in address_form.cleaned_data.values():
                            EmptyFields = True
                    if not EmptyFields:
                        address = address_form.save(commit=False)
                        address.order = order
                        address.save()
                for item in cart:
                    ##not safe chnge to get product by id
                    order_product = Product.objects.get(id = item['id'])
                    order_quantity = item['quantity']
                    OrderItem.objects.create(order = order,product = order_product, quantity = order_quantity)
                    order_product.ReduceAmount(order_quantity)
                cart.clear()
                return redirect('Order/home.html')
    order_form = OrderFormCreate()
    address_form = AdressCreateForm()
    return render(request,'Order/home.html',{ 'cart':cart, 'order_form': order_form, 'address_form':address_form})

