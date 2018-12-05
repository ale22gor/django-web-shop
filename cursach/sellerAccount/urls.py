from django.conf.urls import url

from .views import OrderListView, orderChangeView, productChangeView, ProductListView

urlpatterns = [
    url(r'^orders$', OrderListView.as_view(), name = 'orders'),
    url(r'^(?P<pk>\d+)/change_order$', orderChangeView, name='change_order'),
    url(r'^products$', ProductListView.as_view(), name = 'products'),
    url(r'^(?P<pk>\d+)/change_product$', productChangeView, name='change_product'),
    ##url(r'product_add$', AddProduct, name = 'add_product'),
    ##url(r'product_edit_button$', EditProduct, name = 'edit_product_button'),
    ##url(r'edit_order$', EditOrder, name = 'edit_order'),

]