﻿from django.shortcuts import render
from .forms import BuyForm
from django.views import generic
from products.models import Film
from django.urls import reverse
from cart.views import cart_buy

# Create your views here.

def home_view(request):
    context ={
            
    }
    return render(request,'index.html', context)

class FilmListView(generic.ListView):
    model = Film
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(FilmListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #context['some_data'] = 'This is just some data'        
        return context
    
class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "products/film_detail.html" 

    def get_context_data(self, **kwargs):
        context = super(FilmDetailView, self).get_context_data(**kwargs)
        context['form'] = BuyForm
        return context
    

class BuyView(generic.edit.FormView):
    form_class = BuyForm
    def get_success_url(self):
        cart_buy(self.request)
        return reverse("cart:home")
