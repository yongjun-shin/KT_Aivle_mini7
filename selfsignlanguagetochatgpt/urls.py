# blog/urls.py
from django.urls import path
from . import views

app_name = 'selfsignlanguagetochatgpt'
urlpatterns = [
    path('', views.language, name='index'),
    path('chat', views.chat, name='chat'),
]
