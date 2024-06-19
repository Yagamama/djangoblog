from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView


# def index(request):
#     return render(request, 'index.html', context={'who': 'Lar'})


def about(request):
    return render(request, 'about.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['who'] = 'Lar'
        return context