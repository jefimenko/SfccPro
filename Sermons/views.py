import os

from django.shortcuts import render
from django.views.generic import TemplateView, View
import boto

from common import aws_secrets


class Sermons(TemplateView):

    def get(self, request):
        s3 = boto.s3.connect_to_region(
            'us-west-2',
            aws_access_key_id=aws_secrets.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=aws_secrets.AWS_SECRET_ACCESS_KEY
        )
        bucket = s3.get_bucket('seattlefcc-sermons')

        em_sermon_urls = [
            [
                os.path.basename(key.name),
                s3.generate_url(method='GET', bucket=bucket.name, key=key.name, expires_in=20000000 , force_http=True)
            ]
            for key in bucket.list(prefix='em')
        ][1:]

        return render(
            request,
            'Sermons/templates/sermons.html',
            context={
                'presigned_urls': em_sermon_urls,
            }
        )
