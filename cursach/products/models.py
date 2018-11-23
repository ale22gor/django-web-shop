from django.db import models

# Create your models here.

class Film(models.Model):
    Name = models.CharField(max_length = 64)
    Amount = models.IntegerField()
    Price = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    Descr = models.TextField()
    
