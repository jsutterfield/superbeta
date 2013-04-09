from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Problem, Area, ProblemPhoto, AreaPhoto
from random import choice
from superbeta import weather

def region(request, region_slug):
    try:
        region = Area.objects.get(slug=region_slug)
    except Area.DoesNotExist:
        raise Http404
    return HttpResponse('Welcome to %s!' % region.name)

def area(request, region_slug, area_slug):
    try:
        area = Area.objects.filter(slug=area_slug, area_parent__slug=region_slug).get()
    except Area.DoesNotExist:
        raise Http404
    # photos = area.areaphoto_set.all()
    # problems = area.Problem_set.all()
    # classic_photos = ProblemPhoto.objects.filter(problem__area=area, photo_type="T") 
    # weather_forecast = weather.get_forecast(city=area.closest_city, state=area.state)
    return HttpResponse("Welcome to %s" % area.name)
    # return render(request, 'area.html', {'area': area, 'photos': photos, 'classic_photos': classic_photos, 
    #                                      'weather': weather_forecast})

def boulder(request, region_slug, area_slug, boulder_slug):
    try:
        boulder = Area.objects.filter(slug=boulder_slug, area_parent__slug=area_slug,
                                      area_parent__area_parent__slug=region_slug).get()
    except Area.DoesNotExist:
        raise Http404
    return HttpResponse('Welcome to %s!' % boulder.name)

def problem(request, region_slug, area_slug, boulder_slug, problem_slug):
    try:        
        problem = Problem.objects.filter(slug=problem_slug, parent__slug=boulder_slug,
                                      parent__area_parent__slug=area_slug).get()
    except Area.DoesNotExist:
        raise Http404
    return HttpResponse('Welcome to %s!' % problem.name)
    # problem = None
    # photos = None
    # try:
    #     problem = Problem.objects.get(slug=problem_slug, area__slug=area_slug)
    #     photos = Problem.Problemphoto_set.all()
    # except:
    #     raise Http404
    # return render(request, 'problem.html', {'problem': problem, 'photos': photos})