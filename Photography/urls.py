from django.conf.urls import url, include

from Photography.views import Gallery


urlpatterns = [
    url(r'^$', Gallery.as_view(), name='home'),
]
