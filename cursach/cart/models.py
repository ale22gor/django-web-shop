from django.conf import settings
from django.db import models
from products.models import Film
from django.db.models.signals import post_save
from decimal import Decimal
from django.conf import settings


User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj) 
    def new_or_get(self, request):
        
        qs = self.get_queryset().filter(user = request.user)
        if qs.count() == 1:
            cart_obj = qs.first()
            new_obj = False
        else:
            new_obj = True
            cart = request.session.get(settings.CART_SESSION_ID)
            if not cart:
                cart_obj = Cart.objects.new(user = request.user)
                new_obj = True
            else:
                cart_obj = Cart.objects.new(user = request.user)
                for item in cart:
                    film_obj = Film.objects.get(pk = item)
                    obj_quantity = cart[item]['quantity']
                    Entry.objects.create(cart=cart_obj, product=film_obj, quantity=obj_quantity)
                
        return cart_obj, new_obj




    

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete = 'Cascade')
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)

    objects = CartManager()
    
class Entry(models.Model):
    product = models.ForeignKey(Film, null=True, on_delete='PROTECT')
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, null=True, on_delete='PROTECT')
    
    def __str__(self):
        return str(self.pk)

def update_cart(sender, instance,update_fields = ['cart'], **kwargs):

    list_of_entries = Entry.objects.filter(cart = instance.cart)
    new_cart_cost = 0
    new_cart_count = 0    
    for x in list_of_entries:
        new_cart_cost += int(x.quantity) * Decimal(x.product.Price)
        new_cart_count += int(x.quantity)

    instance.cart.total = new_cart_cost
    instance.cart.count = new_cart_count
    instance.cart.save()

            
post_save.connect(update_cart,sender=Entry) 


 