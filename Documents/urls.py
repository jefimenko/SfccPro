from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from Documents.views import Documents


urlpatterns = [
    url(r'^$', Documents.as_view(), name='Documents.list'),
]
