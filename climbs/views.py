from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Problem, Area, ProblemPhoto, AreaPhoto
from random import choice
import weather

def region(request):
    return HttpResponse('success!')

def area(request, area_slug):
    try:
        area = Area.objects.get(slug=area_slug)
    except Area.DoesNotExist:
        raise Http404
    photos = area.areaphoto_set.all()
    Problems = area.Problem_set.all()
    classic_photos = ProblemPhoto.objects.filter(Problem__area=area, photo_type="T") 
    weather_forecast = weather.get_forecast(city=area.closest_city, state=area.state)
    return render(request, 'area.html', {'area': area, 'photos': photos, 'classic_photos': classic_photos, 
                                         'weather': weather_forecast})

def boulder(request):
    return HttpResponse('success!')

def Problem(request, area_slug, Problem_slug):
    Problem = None
    photos = None
    try:
        Problem = Problem.objects.get(slug=Problem_slug, area__slug=area_slug)
        photos = Problem.Problemphoto_set.all()
    except:
        raise Http404
    return render(request, 'Problem.html', {'Problem': Problem, 'photos': photos})
