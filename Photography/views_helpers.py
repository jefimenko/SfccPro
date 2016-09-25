import os

from PIL import Image, ImageOps


def generateAndSaveThumbnail(original_image_file_name, thumbnail_file_name, thumbnail_size):

    original_image = Image.open(original_image_file_name)
    thumbnail = ImageOps.fit(original_image, thumbnail_size, Image.ANTIALIAS)

    thumbnail.save(thumbnail_file_name, format='JPEG')

def generateLocalThumbnailFileName(prefix, local_original_image_file_name):
    if prefix is None:

        raise ValueError('Prefix unspecified')

    return os.path.join(
        os.path.dirname(local_original_image_file_name),
        prefix,
        os.path.basename(local_original_image_file_name)
    )


def saveThumbnailToS3FromFileName(bucket, prefix, thumbnail_file_name):

    thumbnail_key_name =  os.path.join(
        'gallery/thumbnails',
        prefix,
        os.path.basename(thumbnail_file_name)
    )

    thumbnail_key = bucket.new_key(thumbnail_key_name)
    thumbnail_key.content_type = 'image/jpeg'
    thumbnail_key.set_contents_from_filename(thumbnail_file_name)
