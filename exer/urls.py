# blog/urls.py
from django.urls import path
from . import views

app_name = 'exer'
urlpatterns = [
    path('', views.index, name='index'),
    path('exer1', views.exer1, name='exer1'),
]
