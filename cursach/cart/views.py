from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart, Entry
from products.models import Film
from decimal import Decimal
from .forms import  UpdateForm
from django.views import generic
from django.views.generic.edit import FormView


# Create your views here.






class CartView(generic.ListView):
    def get_queryset(self):
        session = self.request.session
        return Cart.objects.filter(id=user)
    cart_obj = queryset
    model = Entry.objects.filter(cart=cart_obj)
    template_name = "Cart/home.html" 

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['form'] = UpdateForm
        return context
            
            

class UpdateView(FormView):
    form_class = UpdateForm
    
    def cart_update(request):
	    cart_obj, new_obj = Cart.objects.new_or_get(request)
	    cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
	    products = Film.objects.all()
	    if request.POST:
		    entry_id = request.POST.get('id')
		    entry_obj = Entry.objects.get(pk=entry_id)
		    entry_qunatity = request.POST.get('quantity')
		    print(entry_qunatity)
		    if int(entry_qunatity) <= 0:		
			    entry_obj.delete()
		    else:
						
			    entry_obj.quantity = entry_qunatity
			    entry_obj.save()
   
    def get_success_url(self):
        cart_update(self.request)
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
	

	