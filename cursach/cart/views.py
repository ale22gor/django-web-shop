from django.urls import reverse
from .models import Cart, Entry
from products.models import Film
from .forms import  UpdateForm
from django.views import generic

# Create your views here.


class CartView(generic.ListView):
    
    model = Entry
    template_name = "Cart/home.html" 
    
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        # filter by a variable captured from url, for example
        return qs.filter(cart=cart_obj)

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['form'] = UpdateForm
        return context
    
class UpdateView(generic.FormView):
    form_class = UpdateForm
    
    def get_success_url(self):
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
        products = Film.objects.all()
        if self.request.POST:
            entry_id = self.request.POST.get('id')
            entry_obj = Entry.objects.get(pk=entry_id)
            entry_qunatity = self.request.POST.get('quantity')
            if int(entry_qunatity) <= 0:
                entry_obj.delete()
            else:
                        
                entry_obj.quantity = entry_qunatity
                entry_obj.save()
        return reverse("cart:home")
    

def cart_buy(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
    products = Film.objects.all()
    if request.POST:
        product_id = request.POST.get('id')
        product_obj = Film.objects.get(pk=product_id)
        product_quantity = request.POST.get('quantity')
        qs = cart_obj_current_entries.filter(product = product_obj)
        if qs.count() >= 1:
            tmp_entry = qs.first()
            tmp  = tmp_entry.quantity
            tmp += int(product_quantity)
            tmp_entry.quantity = tmp
            tmp_entry.save()
        else:
            Entry.objects.create(cart=cart_obj, product=product_obj, quantity=product_quantity)



