from django.contrib import admin
from models import Problem, ProblemPhoto
from models import Area, AreaPhoto

class AreaPhotoInline(admin.TabularInline):
    model = AreaPhoto


class ProblemPhotoInline(admin.TabularInline):
    model = ProblemPhoto


class AreaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("General Info", {'fields': ['name', 'area_type', 'area_parent', 'city',
            'longitude', 'latitude', 'street_address', 'zipcode']}),
        ('Climbing Available', {'fields': ['bouldering', 'top_rope', 'sport', 
            'trad',]}),
        ('Getting There', {'fields': ['approach_difficulty', 'approach_time', 
            'approach_distance', 'approach_description', 'trailhead_longitude', 
            'trailhead_latitude', 'lot_parking', 'street_parking', 'garage_parking',
            'pullout_parking', 'parking_longitude', 'parking_latitude',
            'parking_description']}),
        ('Climbing Info', {'fields': ['height', 'short_description', 'about',
            'description', 'rock_type']}),
        ('Climbing Season', {'fields': ['spring', 'summer', 'fall', 'winter']}),
        ('Misc Info', {'fields': ['hazard_information', 'pet_friendly', 
            'nearest_emergency', 'nearest_emergency_address', 
            'nearest_emergency_phone', 'slug', 'featured']}),
        ]

    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        AreaPhotoInline
    ]
    list_display = ('name', 'area_type', 'state')
    list_filter = ('area_type', 'featured')
    search_fields = ['name', 'area_type']


class ProblemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ProblemPhotoInline
    ]
    list_filter = ('featured', 'quality') 
    list_display = ('name', 'boulder', 'area', 'region', 'state')
    search_fields = ['name']



admin.site.register(Area, AreaAdmin)
admin.site.register(Problem, ProblemAdmin)
