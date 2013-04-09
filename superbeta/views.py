from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Problem, Area, ProblemPhoto, AreaPhoto
from random import choice
import weather

def home(request):
    featured_Problem = None
    featured_photos = None
    area_photos = None
    try:
        featured_Problem = choice(Problem.objects.filter(featured=True))
    except IndexError:
        pass
    if featured_Problem:
        featured_Problem.has_newline = False
        featured_photos = featured_Problem.Problemphoto_set.all()
        if featured_Problem.description.count('\n', 0, 420) > 0:
            if featured_Problem.description.count('\n', 0, 420) > 1:
                featured_Problem.has_multiple_newlines = True
            else:
                featured_Problem.has_newline = True
        area_photos = AreaPhoto.objects.filter(photo_type="G")
    return render(request, 'index.html', {'featured_Problem': featured_Problem,
                                          'featured_photos': featured_photos,
                                          'area_photos': area_photos}) 