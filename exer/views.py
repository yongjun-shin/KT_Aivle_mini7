from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'exercise/index.html')

def exer1(request):
    return render(request, 'exercise/exer1.html')