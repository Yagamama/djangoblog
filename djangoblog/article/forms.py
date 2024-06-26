from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
        
    # def is_valid(self) -> bool:
    #     return super().is_valid()