from django.conf.urls import url
from .views import  CartView, cart_update, cart_remove


urlpatterns = [
    url(r'^cart_remove/(?P<product_id>\d+)$', cart_remove, name='remove'),
    url(r'^cart_update/$', cart_update, name='update'),
    url(r'^$', CartView.as_view(), name='home'),
]