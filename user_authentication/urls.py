from django.urls import path
from . import views
urlpatterns = [
   #path('add-word', views.insertWord, name='insert-word')
   path('test', views.testView, name='test-view'),
   path('create-user', views.createTest, name = 'test-create')
]
