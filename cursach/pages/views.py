from django.shortcuts import render, get_object_or_404
from cart.forms import UpdateForm
from django.views import generic
from products.models import Product
from comment.forms import CommentForm


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
        context['form'] = UpdateForm(initial = {'id':self.object.pk, 'update' : False}, max_values = {'quantity':self.object.Amount})
        context['comment_form'] = CommentForm()
        
        return context
    
    ## переписать с помощью классов
    def post(self,request, **kwargs):
        form = CommentForm(self.request.POST)
        self.object = self.get_object()
        print(self.object)
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if form.is_valid() and self.request.user.is_authenticated:
            print(request.user)
            comment = form.save(commit=False)
            comment.product = self.object
            comment.author = self.request.user
            comment.save()
        context['form'] = UpdateForm(initial = {'id':self.object.pk, 'update' : False},  max_values = {'quantity':self.object.Amount})
        context['comment_form'] = CommentForm()
        return self.render_to_response(context=context)

    
    
     
        return context

