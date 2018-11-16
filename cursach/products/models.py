from django.db import models

# Create your models here.

class Film(models.Model):
	Name = models.CharField(max_length = 64)
	Amount = models.IntegerField()
	Price = models.IntegerField()
	Descr = models.TextField()
	
