from django.shortcuts import render, redirect
from .forms import OrderFormCreate, AdressCreateForm
from cart.cart import Cart
from .models import OrderItem, Order
from products.models import Product
from django.http import HttpResponse
from django.views import generic
from .tasks import order_created
from datetime import datetime, timedelta

# import celery
from eShop.celeryapp import app as celery_app


# Create your views here.
def create_order(request):
    cart = Cart(request)
    if request.POST:
            order_form = OrderFormCreate(request.POST)
            address_form = AdressCreateForm(request.POST)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                if request.user.is_authenticated:
                    order.user = request.user
                else:
                    order.user = None
                order.save()
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
                    if order_product.Amount < order_quantity:
                        return HttpResponse('Aleady bought')
                    OrderItem.objects.create(order = order,product = order_product, quantity = order_quantity)
                    order_product.ReduceAmount(order_quantity)
                cart.clear()
                order_created.apply_async((order.id,),eta = datetime.now() + timedelta(seconds=10))

                return redirect('Order/home.html')
    order_form = OrderFormCreate()
    address_form = AdressCreateForm()
    return render(request,'Order/home.html',{ 'cart':cart, 'order_form': order_form, 'address_form':address_form})

class OrderList(generic.ListView):
    model = Order
    template_name ="account/order_list.html"
    
    def get_queryset(self):
        queryset = Order.objects.filter(user = self.request.user)
        return queryset
    
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(OrderList, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        
        return context

