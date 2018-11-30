from django.db import models
from products.models import Product

# Create your models here.


class Order(models.Model):
    
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    house = models.CharField(max_length=250)
    flat = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, related_name='items', on_delete = 'Protect')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete = 'Protect', related_name='product_items')
    quantity = models.IntegerField()
    
    def get_cost(self):
        return self.product.Price * self.quantity