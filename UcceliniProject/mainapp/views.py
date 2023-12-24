
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def customize(request):
    return render(request, 'customize.html')