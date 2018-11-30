﻿"""cursach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from pages.views import ProductListView, ProductDetailView
from pages.views import home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home_view),
    url(r'^account/', include(('lk.urls','lk'), namespace='account')),
    url(r'^Products/$', ProductListView.as_view(), name = 'Product-list'),
    url(r'^Product/(?P<pk>\d+)$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
    url(r'^order/', include(('order.urls','order'), namespace='order')),
]
