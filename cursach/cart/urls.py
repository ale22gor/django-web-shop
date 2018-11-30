from django.conf.urls import url
from .views import  CartView, cart_update


urlpatterns = [
    
    url(r'^cart_update/$', cart_update, name='update'),
    url(r'^$', CartView.as_view(), name='home'),
]