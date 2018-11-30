from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
User = settings.AUTH_USER_MODEL


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete = 'Cascade')
    
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

class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete = 'Protect')
    quantity = models.IntegerField()
