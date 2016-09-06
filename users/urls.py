from django.conf.urls import url
from .views import RegisterFormView, LoginFormView

urlpatterns = [
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),

]