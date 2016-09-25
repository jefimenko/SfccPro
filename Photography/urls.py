from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from Photography.views import Gallery, Thumbnails


urlpatterns = [
    url(r'^$', Gallery.as_view(), name='Photography.gallery'),
    url(r'^thumbnails/?$', csrf_exempt(Thumbnails.as_view()), name='Photography.thumbnails'),
]
