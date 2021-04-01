from django.urls import path
from . import views
urlpatterns = [
    path('add-word', views.insertWord, name='insert-word'),
    path('display-all-words', views.DisplayAllWords, name='display-all-words'),
    path('word-game', views.WordGame, name='word-game'),
    path('index', views.index, name = 'index'),
]
