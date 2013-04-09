from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Problem, Area, ProblemPhoto, AreaPhoto
from random import choice
from superbeta import weather

def region(request, region_slug=None):
    return HttpResponse('Welcome to regions!')

def area(request, region_slug=None, area_slug=None):
    return HttpResponse("Welcome to area!")
    # try:
    #     area = Area.objects.get(slug=area_slug)
    # except Area.DoesNotExist:
    #     raise Http404
    # photos = area.areaphoto_set.all()
    # problems = area.Problem_set.all()
    # classic_photos = ProblemPhoto.objects.filter(problem__area=area, photo_type="T") 
    # weather_forecast = weather.get_forecast(city=area.closest_city, state=area.state)
    # return render(request, 'area.html', {'area': area, 'photos': photos, 'classic_photos': classic_photos, 
    #                                      'weather': weather_forecast})

def boulder(request, region_slug=None, area_slug=None, boulder_slug=None):
    return HttpResponse('Welcome to boulder!')

def problem(request, region_slug=None, area_slug=None, boulder_slug=None, problem_slug=None):
    return HttpResponse("Welcome to problem!")
    # problem = None
    # photos = None
    # try:
    #     problem = Problem.objects.get(slug=problem_slug, area__slug=area_slug)
    #     photos = Problem.Problemphoto_set.all()
    # except:
    #     raise Http404
    # return render(request, 'problem.html', {'problem': problem, 'photos': photos})