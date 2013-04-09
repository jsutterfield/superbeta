from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from climbs.models import Problem, Area, ProblemPhoto, AreaPhoto
from random import choice
import weather

def home(request):
    featured_problem = None
    featured_photos = None
    area_photos = None
    try:
        featured_problem = choice(Problem.objects.filter(featured=True))
    except IndexError:
        pass
    if featured_problem:
        featured_problem.has_newline = False
        featured_photos = featured_problem.problemphoto_set.all()
        if featured_problem.description.count('\n', 0, 420) > 0:
            if featured_problem.description.count('\n', 0, 420) > 1:
                featured_problem.has_multiple_newlines = True
            else:
                featured_problem.has_newline = True
    area_photos = AreaPhoto.objects.filter(area__area_type='AR', area__featured=True)
    return render(request, 'index.html', {'featured_problem': featured_problem,
                                          'featured_photos': featured_photos,
                                          'area_photos': area_photos}) 