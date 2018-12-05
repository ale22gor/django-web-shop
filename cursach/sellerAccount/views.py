from django.shortcuts import render
from order.models import Order
from products.models import Product
from .forms import OrderEditForm, ProductEditForm
from django.views import generic
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
class OrderListView(generic.ListView):
    model = Order
    paginate_by = 10
    template_name = "seller/order_list.html" 

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(OrderListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #context['some_data'] = 'This is just some data'        
        return context
    

    
def orderChangeView(request,pk):
    instance = get_object_or_404(Order, id=pk)
    form = OrderEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home/')
    return render(request, 'seller/Order_detail.html', {'form': form,'id':pk}) 
    
class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
    template_name = "seller/product_list.html" 

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #context['some_data'] = 'This is just some data'        
        return context

def productChangeView(request,pk):
    instance = get_object_or_404(Product, id=pk)
    form = ProductEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home/')
    return render(request, 'seller/Product_detail.html', {'form': form,'id':pk}) 

    