from django.shortcuts import render
from django.views.generic import TemplateView


class Dashboard(TemplateView):

    def get(self, request):

        return render(request=request, template_name='SfccUser/templates/dashboard.html', context={})
