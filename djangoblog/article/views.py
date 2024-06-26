from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Article
from .forms import ArticleForm


# def index(request):
#     name = 'Djangoblog'
#     return render(request, 'articles/index.html', context={'name':name})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        name = 'Djangoblog'
        a = Article.objects.all()
        return render(request, 'articles/index.html', context={'name': name, 'article': a})
    

def article_id(request, article_id):
    a = Article.objects.filter(id=article_id).first()
    return render(request, 'articles/art.html', context={'article': a})


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})
    