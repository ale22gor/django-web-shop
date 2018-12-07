from django.conf.urls import url
from .views import   create_order


urlpatterns = [    
    url(r'^$', create_order, name='home'),

]