from django.shortcuts import render, redirect

def verify(request):
    return render(request, 'verify/verify.html')