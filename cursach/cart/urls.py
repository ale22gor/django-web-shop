from django.conf.urls import url
from .views import  CartView, UpdateView


urlpatterns = [
    
    url(r'^cart_update/$', UpdateView.as_view(), name='update'),
    url(r'^$', CartView.as_view(), name='home'),
]