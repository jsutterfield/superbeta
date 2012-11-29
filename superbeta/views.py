from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html') 

def pic(request):
    image_data = open("/home/jafaraf/Pictures/2011/08/25/dad2.jpg", "rb").read()
    return HttpResponse(image_data, mimetype="image/jpg")
