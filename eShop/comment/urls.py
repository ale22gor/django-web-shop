from django.conf.urls import url
from .views import comment_approve, comment_remove


urlpatterns = [    
    url(r'^approve/(?P<pk>\d+)$', comment_approve, name='approve'),
    url(r'^remove/(?P<pk>\d+)$', comment_remove, name='remove'),
]

