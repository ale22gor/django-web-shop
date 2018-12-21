from cart.forms import UpdateForm
from django.views import generic
from .models import Product
from comment.forms import CommentForm
from comment.models import Comment
from django.http import Http404



class ProductListView(generic.ListView):
    model = Product
    paginate_by = 10
    def get_queryset(self):
        if self.request.GET:
            category = self.request.GET['category']
            if category:
                queryset = Product.objects.filter(Category = category)
                if not queryset:
                    raise Http404("No Category matches the given query.")
                return queryset
        queryset = Product.objects.all()
        return queryset

    
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['categories'] = [x[1] for x in Product.CATEGORY_CHOICES]
        if self.request.GET:
            context['category'] = self.request.GET['category']
        else:
            context['category'] = None
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
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if form.is_valid() and self.request.user.is_authenticated :
            qs = Comment.objects.filter(author=request.user).filter(product = self.object)
            if qs.count() < 1:
                comment = form.save(commit=False)
                comment.product = self.object
                comment.author = self.request.user
                comment.save()
        context['form'] = UpdateForm(initial = {'id':self.object.pk, 'update' : False},  max_values = {'quantity':self.object.Amount})
        context['comment_form'] = CommentForm()
        return self.render_to_response(context=context)


