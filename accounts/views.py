# accounts/views.py
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 

def index(request):
    return render(request, 'sign/index.html')

def exer(request):
    return render(request, 'sign/exer.html')

def signup(request): 
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2']: 
            user = User.objects.create_user( 
                username=request.POST['username'], 
                password=request.POST['password1'], 
                email=request.POST['email'],
            ) 
            auth.login(request, user) 
            return redirect('/') 
        return render(request, 'sign/signup.html') 
    else: 
        form = UserCreationForm 
        return render(request, 'sign/signup.html', {'form':form})