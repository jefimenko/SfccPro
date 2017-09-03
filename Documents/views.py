from django.shortcuts import render
from django.views.generic import TemplateView, View


class Documents(TemplateView):

    def get(request):

        return render(
            request,
            'Documents/templates/documents_list.html'
        )
