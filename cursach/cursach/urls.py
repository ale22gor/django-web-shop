"""cursach URL Configuration

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
from pages.views import FilmListView, FilmDetailView
from pages.views import BuyView

from pages.views import home_view, register_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home_view),
	path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register$', register_view),
    url(r'^films/$', FilmListView.as_view(), name = 'film-list'),
    url(r'^film/(?P<pk>\d+)$', FilmDetailView.as_view(), name='book-detail'),
	url(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
	url(r'^buy_form/$', BuyView.as_view(), name='buy_form_url'),

]
