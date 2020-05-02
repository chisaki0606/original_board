from django.urls import path
from .import views

app_name = 'board'

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),  
]