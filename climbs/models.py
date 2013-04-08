from django.db import models 
from autoslug import AutoSlugField
from django.contrib.localflavor.us.models import USStateField

def save_area(instance, file_name):
    return "photos/%s/%s/%s" % (instance.area.state, instance.area.name, file_name)

def save_route(instance, file_name):
    return "photos/%s/%s/%s/%s" % (instance.route.parent.state, instance.route.parent.name, instance.route.name, file_name)

class Area(models.Model):
    AREA_CHOICES = (
        ("RE", "Region"),
        ("AR", "Area"),
        ("BO", "Boulder")
    )
    APPROACH_CHOICES = (
        ("Easy", "Flip Flops"),
        ("Intermediate", "Sneakers"),
        ("Difficult", "Boots")
    )
    PARKING_TYPE = (
        ("L", "Lot"),
        ("S", "Street"),
        ("G", "Garage")
    )
    name = models.CharField(max_length=100)
    area_type = models.CharField(max_length=2, choices=AREA_CHOICES)
    area_parent = models.ForeignKey("self", null=True, blank=True)
    state = USStateField()
    city = models.CharField(max_length=20, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    street_address = models.CharField(max_length=40, blank=True)
    zipcode = models.SmallIntegerField(null=True, blank=True)
    bouldering = models.BooleanField(default=False, blank=True)
    top_rope = models.BooleanField(default=False, blank=True)
    sport = models.BooleanField(default=False, blank=True)
    trad = models.BooleanField(default=False, blank=True)
    approach_difficulty = models.CharField(max_length=12, choices=APPROACH_CHOICES, blank=True)
    approach_time = models.SmallIntegerField(null=True, blank=True)
    approach_distance = models.SmallIntegerField(null=True, blank=True)
    approach_description = models.TextField(blank=True)
    trailhead_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    trailhead_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_type = models.CharField(max_length=1, choices=PARKING_TYPE, blank=True)
    parking_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_description = models.CharField(max_length=750, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)
    description = models.TextField(blank=True)
    rock_type = models.CharField(max_length=25, blank=True)
    weather_description = models.CharField(max_length=500, blank=True)
    climbing_season = models.CharField(max_length=500, blank=True)
    hazard_information = models.CharField(max_length=750, blank=True)
    misc_information = models.CharField(max_length=750, blank=True)
    pet_friendly = models.BooleanField(default=False)
    nearest_emergency = models.CharField(max_length=25, blank=True)
    nearest_emergency_address = models.CharField(max_length=40, blank=True)
    nearest_emergency_phone = models.SmallIntegerField(null=True, blank=True)
    nearest_emergttency_two_address = models.CharField(max_length=40, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='state')
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s -- %s" % (self.name, self.state)

    
class Route(models.Model):
    ROUTE_QUALITY = (
        # Look into having the first value be nums, not strings.
        ('1', "One Star"),
        ('2', "Two Star"),
        ('3', "Three Star"),
        ('4', "Four Star"),
        ('5', "Five Star")
    )
    ANGLE_CHOICES = (
        ('S', 'Slab'),
        ('N', '90 Degrees'),
        ('O', 'Overhang'),
        ('R', 'Roof')
    )
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Area')
    featured = models.BooleanField(default=False)
    grade = models.CharField(max_length=6)
    quality = models.CharField(max_length=1, choices=ROUTE_QUALITY, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField(blank=True)
    quality_rating = models.CharField(max_length=1, choices=ROUTE_QUALITY, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    angle = models.CharField(max_length=1, choices=ANGLE_CHOICES, blank=True)
    features = models.CharField(max_length=40, blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    route_start = models.CharField(max_length=100, blank=True)
    route_descent = models.CharField(max_length=100, blank=True)
    landing_information = models.CharField(max_length=100, blank=True)
    hazard_information = models.CharField(max_length=100, blank=True)
    aspect = models.CharField(max_length=50, blank=True)
    variations = models.CharField(max_length=100, blank=True)
    misc_information = models.CharField(max_length=100, blank=True)
    first_ascent = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/areas/%s/%s" % (self.area.slug, self.slug)

    def validate_rating(self):
        pass


class RoutePhoto(models.Model):
    PHOTO_CHOICES = (
        ("O", "Overview"),
        ("G", "General")
    )
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    route = models.ForeignKey('Route')
    photo = models.ImageField(upload_to=save_route)

    def __unicode__(self):
        return "%s-%s" % (self.route, self.photo_type)


class AreaPhoto(models.Model):
    PHOTO_CHOICES = (
        ("G", "General"),
        ("A", "Approach"),
    )
    area = models.ForeignKey('Area')
    photo = models.ImageField(upload_to=save_area)
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)

    def __unicode__(self):
        return "%s-%s" % (self.area, self.photo_type)