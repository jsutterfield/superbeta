from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Route, Area, RoutePhoto, AreaPhoto
from random import choice
import weather

def home(request):
    featured_route = choice(Route.objects.filter(featured=True))
    featured_route.has_newline = False
    featured_photos = featured_route.routephoto_set.all()
    if featured_route.description.count('\n', 0, 420) > 0:
        if featured_route.description.count('\n', 0, 420) > 1:
            featured_route.has_multiple_newlines = True
        else:
            featured_route.has_newline = True
    area_photos = AreaPhoto.objects.filter(photo_type="G")
    return render(request, 'index.html', {'featured_route': featured_route,
                                          'featured_photos': featured_photos,
                                          'area_photos': area_photos}) 

def route(request, area_slug, route_slug):
    route = None
    photos = None
    try:
        route = Route.objects.get(slug=route_slug, area__slug=area_slug)
        photos = route.routephoto_set.all()
    except:
        raise Http404
    return render(request, 'route.html', {'route': route, 'photos': photos})

def area(request, area_slug):
    try:
        area = Area.objects.get(slug=area_slug)
    except Area.DoesNotExist:
        raise Http404
    photos = area.areaphoto_set.all()
    routes = area.route_set.all()
    classic_photos = RoutePhoto.objects.filter(route__area=area, photo_type="T") 
    weather_forecast = weather.get_forecast(city=area.closest_city, state=area.state)
    return render(request, 'area.html', {'area': area, 'photos': photos, 'classic_photos': classic_photos, 
                                         'weather': weather_forecast})