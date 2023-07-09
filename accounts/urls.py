from django.urls import path 
from . import views 

app_name = 'accounts'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('exer', views.exer, name='exer'),
	path('signup', views.signup, name='signup'),
]