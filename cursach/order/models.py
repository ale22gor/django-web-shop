from django.db import models

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
