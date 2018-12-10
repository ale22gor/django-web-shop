from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Comment(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    
    product = models.ForeignKey(Product, related_name='comments', on_delete = 'Protect')
    author = models.ForeignKey(User, on_delete = 'Protect')
    text = models.TextField()
    rating = models.DecimalField(default = 1, choices = RATING_CHOICES, max_digits=3, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
class CommentSummary(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Comment Summary'
        verbose_name_plural = 'Comments Summary'