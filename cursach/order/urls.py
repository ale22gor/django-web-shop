from django.conf.urls import url
from .views import   create_order, create_address


urlpatterns = [    
    url(r'^$', create_order, name='home'),
    url(r'^address$', create_address, name='address'),

]