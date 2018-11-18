from django.shortcuts import render, redirect

from .models import Cart, Entry
from products.models import Film
from decimal import Decimal


# Create your views here.



def cart_home(request):
	""" This view displays what is in a user's cart. """
    # Based on the user who is making the request, grab the cart object
	cart_obj = Cart.objects.new_or_get(request)
    # Get a queryset of entries that correspond to "my_cart"
	##list_of_entries = Entry.objects.filter(cart = cart_obj)
	# Make a list of the product's names
	##list_of_products = list(list_of_entries.values_list('product__name', flat=True))
	# Remove redundant product names
	##list_of_products = list(set(list_of_products))
	##return render(request, 'something.html', {'list_of_products': list_of_products})
	return render(request, "Cart/home.html", {})

def cart_update(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	cart_obj_current_entries = Entry.objects.filter(cart=cart_obj)
	products = Film.objects.all()
	if request.POST:
		product_id = request.POST.get('id')
		product_obj = Film.objects.get(pk=product_id)
		product_quantity = request.POST.get('quantity')
		qs = cart_obj_current_entries.filter(product = product_obj)
		if qs.count() >= 1:
			line_cost = int(product_quantity) * Decimal(product_obj.Price)
			cart_obj.total = Decimal(cart_obj.total) + line_cost
			cart_obj.count = int(cart_obj.count) + int(product_quantity)
			cart_obj.save()
			print(qs.first())
			tmp_entry = qs.first()
			tmp  = tmp_entry.quantity
			tmp += int(product_quantity)
			
			tmp_entry.quantity = tmp
			tmp_entry.save()
			print(qs.first().quantity)
		else:
			Entry.objects.create(cart=cart_obj, product=product_obj, quantity=product_quantity)
	
	