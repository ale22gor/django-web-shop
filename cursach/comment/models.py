from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
User = settings.AUTH_USER_MODEL


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete = 'Protect')
    author = models.ForeignKey(User, on_delete = 'Protect')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text