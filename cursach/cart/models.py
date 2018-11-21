from django.conf import settings
from django.db import models
from products.models import Film
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal


User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj) 
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id",None)
        print(cart_id)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            new_obj = False
            if request.user.is_authenticated:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user = request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        
        return cart_obj, new_obj

class EntryManager(models.Manager):
    def new_or_get(self,cart_id):
        self.cart.get_queryset().filter(id = cart_id)


    

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


 