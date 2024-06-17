from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = 'Djangoblog'
    return render(request, 'articles/index.html', context={'name':name})
