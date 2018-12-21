from django.shortcuts import render
from products.models import Product
from django.views import generic



    
class SearchListView(generic.ListView):
    model = Product
    paginate_by = 10
    template_name = "search_list.html"
    def get_queryset(self):
        if self.request.GET:
            product_name = self.request.GET['product_name']
            if product_name:
                queryset = Product.objects.filter(Name__icontains = product_name)
                return queryset
        queryset = Product.objects.none()
        return queryset

    
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(SearchListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        return context