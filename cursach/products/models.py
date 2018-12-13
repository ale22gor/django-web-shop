from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Commedy', 'Commedy'),
    )
    Name = models.CharField(max_length = 64)
    Amount = models.IntegerField()
    Price = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    Descr = models.TextField()
    PurchaisePrice = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    Category = models.CharField(null=True, blank=True, max_length=10, choices=CATEGORY_CHOICES)
    Image = models.ImageField(upload_to='static/products/%Y/%m/%d',blank=True)
    
    def ReduceAmount(self,value):
        self.Amount -= value
        self.save()

    def IncreaseAmount(self,value):
        self.Amount += value
        self.save()
    
    def get_absolute_url(self):
        return reverse('product:detail', args=[str(self.id)])
    
    def __str__(self):
        return self.Name
