from celery import task
from .models import OrderItem, Order

@task
def order_created(order_id):

    for item in OrderItem.objects.filter(order__id = order_id):
        item.product.IncreaseAmount(item.quantity)
