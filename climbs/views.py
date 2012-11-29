from django.shortcuts import render
from models import Route, Photo

def shamus(request):
    obj = Route.objects.get()
    photos = Photo.objects.all()
    return render(request, 'route.html', {'route': obj, 'photos': photos})

def show_route(request, slug):
    route = Route.objects.get(slug=slug)
    photos = route.photo_set.all()
    return render(request, 'shamus.html', {'route': route, 'photos': photos})

"""
from routes.models import Route, Photo
e = Route.objects.get(pk=1)
p = e.photo_set.all()
"""
