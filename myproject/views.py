# myproject/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cv_view(request):
    return render(request, 'cv.html')