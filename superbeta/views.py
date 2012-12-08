from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Route, Area, RoutePhoto, AreaPhoto
from random import choice

def home(request):
    featured_route = choice(Route.objects.filter(featured=True))
    featured_route.has_newline = False
    featured_photos = featured_route.routephoto_set.all()
    if '\n' in featured_route.description[:420]:
        featured_route.has_newline = True
    return render(request, 'index.html', {'featured_route': featured_route,
                                          'featured_photos': featured_photos}) 

def route(request, area_slug, route_slug):
    route = None
    photos = None
    try:
        route = Route.objects.get(slug=route_slug, area__slug=area_slug)
        photos = route.routephoto_set.all()
    except:
        raise Http404
    return render(request, 'route2.html', {'route': route, 'photos': photos})

def area(request, area_slug):
    try:
        a = Area.objects.get(slug=area_slug)
    except Area.DoesNotExist:
        raise Http404
    return render(request, 'area.html')

"""
from routes.models import Route, Photo
e = Route.objects.get(pk=1)
p = e.photo_set.all()
"""


"""
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
"""