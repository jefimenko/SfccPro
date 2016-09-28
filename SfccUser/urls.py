from django.conf.urls import url, include

from SfccUser.views import Dashboard

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='SfccUser.dashboard'),
]
