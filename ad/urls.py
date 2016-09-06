from django.conf.urls import url
from .views import AdListView, AdDetailView

urlpatterns = [
    url(r'^$', AdListView.as_view(), name='ad_list'),
    url(r'^(?P<pk>[0-9]+)/$', AdDetailView.as_view(), name='ad_detail'),
]