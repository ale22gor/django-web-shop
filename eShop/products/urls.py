from django.conf.urls import url
from .views import ProductListView, ProductDetailView


urlpatterns = [    
    url(r'^$', ProductListView.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)$', ProductDetailView.as_view(), name='detail'),
]