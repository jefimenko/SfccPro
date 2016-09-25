import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
import boto

from Photography import views_helpers


class Gallery(TemplateView):

    def get(self, request):
        s3 = boto.s3.connect_to_region('us-west-2')

        bucket = s3.get_bucket('seattlefcc-photos')

        presigned_urls = [
            s3.generate_url(method='GET', bucket=bucket.name, key=key.name, expires_in=20000000 , force_http=True)
            for key in bucket.list(prefix='gallery/thumbnails')
        ][1:]

        # TODO: crop/resize images?

        return render(request, 'Photography/templates/gallery.html', context={'presigned_urls': presigned_urls})

class Thumbnails(View):

    # TODO: Require log in
    def post(self, request):
        file_name = json.loads(request.body.decode('utf-8')).get('file_name')

        if not file_name:

            return JsonResponse({'status': 'error', 'message': 'Missing file_name'} , status=400)

        # Get image from S3
        s3 = boto.s3.connect_to_region('us-west-2')
        bucket = s3.get_bucket('seattlefcc-photos')
        key = bucket.get_key(os.path.join('gallery', 'fullsize', file_name))

        if key is None:

            return JsonResponse({'status': 'error', 'message': 'Image not found'} , status=404)

        local_original_image_file_name = os.path.join(settings.MEDIA_ROOT, 'thumbnails_temp', os.path.basename(key.name))
        key.get_contents_to_filename(local_original_image_file_name)


        # Generate thumbnails
        small_thumbnail_file_name = views_helpers.generateLocalThumbnailFileName('200', local_original_image_file_name)
        small_thumbnail_size = (200, 200)
        views_helpers.generateAndSaveThumbnail(local_original_image_file_name, small_thumbnail_file_name, small_thumbnail_size)

        medium_thumbnail_file_name = views_helpers.generateLocalThumbnailFileName('400', local_original_image_file_name)
        medium_thumbnail_size = (400, 400)
        views_helpers.generateAndSaveThumbnail(local_original_image_file_name, medium_thumbnail_file_name, medium_thumbnail_size)


        # Save thumbnails to S3
        views_helpers.saveThumbnailToS3FromFileName(bucket, '200', small_thumbnail_file_name)
        views_helpers.saveThumbnailToS3FromFileName(bucket, '400', medium_thumbnail_file_name)

        # Clear downloaded/generated thumbnail files
        os.remove(local_original_image_file_name)
        os.remove(small_thumbnail_file_name)
        os.remove(medium_thumbnail_file_name)

        return JsonResponse({'status': 'success'}, status=201)
