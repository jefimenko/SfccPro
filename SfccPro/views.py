from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView


class Home(TemplateView):

    def get(self, request):
        banner_image_url = 'http://seattlefcc.pro.s3-us-west-2.amazonaws.com/24.jpg?Signature=omujZMy%2BlvKfxBKvQRAziIDVxDM%3D&Expires=1475191159&AWSAccessKeyId=AKIAI5J3BFO5Q334A53Q'

        return render(
            request=request,
            template_name='SfccPro/templates/index.html',
            context={'banner_image_url': banner_image_url}
        )
