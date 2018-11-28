from django.urls import reverse
from .models import Cart, Entry
from products.models import Film
from .forms import  UpdateForm
from django.views import generic
from .cart import CartInSession

# Create your views here.


class CartView(generic.ListView):
    
    model = Entry
    template_name = "Cart/home.html" 
    
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        if  (self.request.user.is_authenticated):
            cart_obj,new_obj = Cart.objects.new_or_get(self.request)
            return qs.filter(cart=cart_obj)
        # filter by a variable captured from url, for example
        

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        if not (self.request.user.is_authenticated):
            context['cart'] = CartInSession(self.request)
        context['form'] = UpdateForm
        return context
    
class UpdateView(generic.FormView):
    form_class = UpdateForm
    
    def get_success_url(self):
        
        if self.request.POST:
            entry_id = self.request.POST.get('id')
            entry_qunatity = self.request.POST.get('quantity')
            if self.request.user.is_authenticated:
                
                entry_obj = Entry.objects.get(pk=entry_id)
            
                cart_obj, new_obj = Cart.objects.new_or_get(self.request)
                cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
                products = Film.objects.all()
                if int(entry_qunatity) <= 0:
                    entry_obj.delete()
                else:
                        
                    entry_obj.quantity = entry_qunatity
                    entry_obj.save()
            else:
                cart = CartInSession(self.request)
                print(entry_qunatity)
                product_price = Film.objects.get(pk=entry_id).Price
                if int(entry_qunatity) > 0:
                    cart.add(product=entry_id, price = product_price, quantity=entry_qunatity,  update_quantity=True)
                else:
                    cart.remove(product=entry_id)
        return reverse("cart:home")
    

def cart_buy(request):
    
    if request.POST:
        product_id = request.POST.get('id')
        product_quantity = request.POST.get('quantity')
        if request.user.is_authenticated:
            cart_obj, new_obj = Cart.objects.new_or_get(request)
            cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
            product_obj = Film.objects.get(pk=product_id)
            qs = cart_obj_current_entries.filter(product = product_obj)
            if qs.count() >= 1:
                tmp_entry = qs.first()
                tmp  = tmp_entry.quantity
                tmp += int(product_quantity)
                tmp_entry.quantity = tmp
                tmp_entry.save()
            else:
                Entry.objects.create(cart=cart_obj, product=product_obj, quantity=product_quantity)
        else:
            cart = CartInSession(request)
            product_price = Film.objects.get(pk=product_id).Price
            cart.add(product=product_id, price = product_price, quantity=product_quantity,  update_quantity=False)
            return reverse('cart:home')



