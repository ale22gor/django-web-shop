from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Order(models.Model):
     
    user = models.ForeignKey(User, null=True, blank=True, on_delete = 'Protect')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    
    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, related_name='items', on_delete = 'Cascade')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete = 'Protect', related_name='product_items')
    quantity = models.IntegerField()
    
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True, auto_now=True)
    
    def get_cost(self):
        return self.product.Price * self.quantity
    
class Adress(models.Model):
    order = models.OneToOneField(Order, null=True, blank=True, related_name='order', on_delete = 'Cascade')
    city = models.CharField(max_length=250, blank=True, null=True)
    street = models.CharField(max_length=250, blank=True, null=True)
    house = models.CharField(max_length=250, blank=True, null=True)
    flat = models.CharField(max_length=250, blank=True, null=True)
    
class OrderSummary(OrderItem):
    class Meta:
        proxy = True
        verbose_name = 'Order Summary'
        verbose_name_plural = 'Orders Summary'