from django.conf.urls import url
from django.urls import include
from django.contrib.auth.views import logout
from order.views import OrderList
from .views import login_view, register_view, home_view, edit_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^login/$', login_view, name = 'login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^$', home_view, name='home'),
    url(r'edit$', edit_view, name = 'edit'),
    url(r'order_list$', login_required(OrderList.as_view()), name = 'order_list'),

]