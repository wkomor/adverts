from django.conf.urls import url
from .views import AdListView, AdDetailView, AdAdd, AdUpdate

urlpatterns = [
    url(r'^$', AdListView.as_view(), name='ad_list'),
    url(r'^(?P<pk>[0-9]+)/$', AdDetailView.as_view(), name='ad_detail'),
    url(r'^add/$', AdAdd.as_view(), name='add_ad'),
    url(r'^update/(?P<pk>[0-9]+)/$', AdUpdate.as_view(), name='ad_update'),
]