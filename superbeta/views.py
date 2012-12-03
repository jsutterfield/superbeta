from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html') 

def route(request):
    return render(request, 'route.html')

def area(request):
    return render(request, 'area.html')