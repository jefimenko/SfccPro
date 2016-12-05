from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from Sermons.views import Sermons


urlpatterns = [
    url(r'^$', Sermons.as_view(), name='Sermons.sermons'),
]
