from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


class Home(TemplateView):
    def get(self, request):
        return render_to_response('SfccPro/templates/index.html', context_instance=RequestContext(request))
