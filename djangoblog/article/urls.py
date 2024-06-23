from django.urls import path
from djangoblog.article import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('article_id/<int:article_id>/', views.article_id, name='tag_and_article'),
]