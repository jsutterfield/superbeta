from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from climbs.models import Route

def home(request):
    return render(request, 'index.html') 

def route(request, slug):
    exists = True
    topo = None
    overhead = None
    if not slug:
        return render(request, 'route.html')
    else:
        route = {'name': 'Not Found', 'difficulty': 'v0',
                 'description': 'Sorry, %s was not found in the database, please try again.' % slug }
        try:
            route = Route.objects.get(slug=slug)
        except Route.DoesNotExist:
            exists = False
    if exists:
        topo = route.routephoto_set.filter(photo_type="T").get()
        overhead = route.routephoto_set.filter(photo_type='C').get()
    return render(request, 'route2.html', {'route': route, 'topo': topo, 'overhead': overhead})

def area(request):
    return render(request, 'area.html')

"""
from routes.models import Route, Photo
e = Route.objects.get(pk=1)
p = e.photo_set.all()
"""