from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from products.models import Product
from .forms import  UpdateForm
from django.views import generic
from .cart import Cart
from django.views.decorators.http import require_POST
# Create your views here.


class CartView(generic.TemplateView):
    
    template_name = "Cart/home.html" 
    
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart =  Cart(self.request)
        product_id = cart.get_all_products_id()
        if len(product_id) > 0:
            products = get_list_or_404(Product, id__in = cart.get_all_products_id())
            for item in cart:
                id = int(item['id'])
                product = [product for product in products if product.id == id]
                if len(product) == 1:
                    amount = product[0].Amount
                    item['update_quantity_form'] = UpdateForm(initial={'id':item['id'], 'quantity': item['quantity'],'update': True},
                                                              max_values = {'quantity':amount})       
        context['cart'] = Cart(self.request)
        return context
    
@require_POST
def cart_update(request):
    cart = Cart(request)
    form = UpdateForm(data=request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        product = get_object_or_404(Product, id=cd['id'])
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('cart:home')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:home')


