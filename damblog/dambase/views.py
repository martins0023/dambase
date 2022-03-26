from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'dambase/home.html')

def about(request):
    return render(request, 'dambase/about.html')