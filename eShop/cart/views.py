from django.shortcuts import get_object_or_404, redirect
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
        for item in cart:
            product = get_object_or_404(Product, id=item['id'])
            item['update_quantity_form'] = UpdateForm(initial={'id':item['id'], 'quantity': item['quantity'],'update': True}, max_values = {'quantity':product.Amount})
        context['cart'] = Cart(self.request)
        return context
    
@require_POST
def cart_update(request):
    cart = Cart(request)
    print(request.POST)
    form = UpdateForm(data=request.POST)
    print(form.is_valid())
    
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


