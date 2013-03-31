from django.db import models 
from autoslug import AutoSlugField
from django.contrib.localflavor.us.models import USStateField

class Area(models.Model):
    AREA_CHOICES = (
        ("RE", "Region"),
        ("AR", "AREA"),
        ("WA", "Wall")
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
    area_type = models.CharField(max_length=2, choices=AREA_CHOICES)
    area_parent = models.ManyToManyField("self")
    state = USStateField()
    city = models.CharField(max_length=20)
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
    approach_description = models.CharField(blank=True)
    trailhead_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    trailhead_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_type = models.CharField(max_length=1, choices=PARKING_TYPE, blank=True)
    parking_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_description = models.CharField(blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    about = models.CharField(blank=True)
    description = models.CharField(blank=True)
    rock_type = models.CharField(blank=True)
    weather_description = models.CharField(blank=True)
    climbing_season = models.CharField(blank=True)
    hazard_information = models.CharField(blank=True)
    misc_information = models.CharField(blank=True)
    pet_friendly = models.BooleanField(default=False)
    nearest_emergency = models.CharField(blank=True)
    nearest_emergency_address = models.CharField(max_length=40, blank=True)
    nearest_emergency_phone = models.SmallIntegerField(null=True, blank=True)
    nearest_emergttency_two_address = models.CharField(max_length=40, blank=True)
    slug = AutoSlugField(populate_from='name', unique_with='area__name')
    featured = models.BooleanField(default=False)

    
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
    parent = ForeignKey('Area')
    grade = models.CharField(max_length=6)
    quality = models.CharField(max_length=1, choices=ROUTE_QUALITY, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField(blank=True)
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    angle = models.CharField(max_length=1, choices=ANGLE_CHOICES, blank=True)
    features = models.CharField(blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    about = models.CharField(blank=True)
    location = models.CharField(blank=True)
    route_start = models.CharField(blank=True)
    route_descent = models.CharField(blank=True)
    landing_information = models.CharField(blank=True)
    hazard_information = models.CharField(blank=True)
    aspect = models.CharField(blank=True)
    variations = models.CharField(blank=True)
    misc_information = models.CharField(blank=True)
    first_ascent = models.CharField(blank=True)
    source = models.CharField(blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/areas/%s/%s" % (self.area.slug, self.slug)

    def validate_rating(self):
        pass


class RoutePhoto(models.Model):

    PHOTO_CHOICES = (
        ("T", "Topo"),
        ("B", "Beta"),
        ("C", "Context"),
        ("G", "General")
    )
    
    # Figure out a better naming scheme for where the photos
    # are uploaded to
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    route = models.ForeignKey('Route')
    # Look into changing this field - chartype doesn't seem right
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)
    photo = models.ImageField(upload_to="photos")

    def __unicode__(self):
        return "%s-%s" % (self.route, self.photo_type)


class AreaPhoto(models.Model):
    PHOTO_CHOICES = (
        ("G", "General"),
        ("A", "Approach"),
    )
    area = models.ForeignKey('Area')
    photo = models.ImageField(upload_to="photos")
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)

    def __unicode__(self):
        return "%s-%s" % (self.area, self.photo_type)