from django.urls import path
from djangoblog.article import views

urlpatterns = [
    path('', views.index)
]