from django.urls import path
from . import views
urlpatterns = [
    path('add-word', views.insertWord, name='insert-word')
]
