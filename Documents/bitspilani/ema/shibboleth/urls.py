import django
from django.conf.urls import url

from .views import ShibbolethView, ShibbolethLogoutView, ShibbolethLoginView, WilpShibbolethLogoutView

app_name = 'shibboleth'

urlpatterns = [
    url(r'^login/$', ShibbolethLoginView.as_view(), name='login'),
    url(r'^logout/$', ShibbolethLogoutView.as_view(), name='logout'),
    url(r'^wilp-logout/$', WilpShibbolethLogoutView.as_view(), name='wilp-logout'),
    url(r'^$', ShibbolethView.as_view(), name='info'),
]
