from django.conf.urls import url

from .views import *

urlpatterns = [

    url(r'^items/$', ItemViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^items/(?P<pk>\d+)$', ItemViewSet.as_view({'get': 'retrieve', 'put':'partial_update', 'delete':'destroy'})),

    url(r'^events/$', EventViewSet.as_view({'get':'list', 'post':'create'})),
    url(r'^events/(?P<pk>\d+)$', EventViewSet.as_view({'get': 'retrieve', 'put':'partial_update', 'delete':'destroy'})),
]
