import os

import boto
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Gallery(TemplateView):

    def get(self, request):
        s3 = boto.s3.connect_to_region('us-west-2')

        bucket = s3.get_bucket('seattlefcc-photos')

        presigned_urls = [
            s3.generate_url(method='GET', bucket=bucket.name, key=key.name, expires_in=20000000 , force_http=True)
            for key in bucket.list(prefix='gallery')
        ][1:]

        # TODO: crop/resize images?

        return render(request, 'Photography/templates/gallery.html', context={'presigned_urls': presigned_urls})
