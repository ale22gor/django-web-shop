from django.shortcuts import render
from cart.forms import UpdateForm
from django.views import generic
from products.models import Product

# Create your views here.

def home_view(request):
    context ={
            
    }
    return render(request,'index.html', context)

class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #context['some_data'] = 'This is just some data'        
        return context
    
class ProductDetailView(generic.DetailView):
    
    model = Product
    template_name = "products/Product_detail.html" 
    def get_context_data(self, **kwargs):
        
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = UpdateForm(initial = {'id':kwargs['object'].id, 'update' : False})
        return context

