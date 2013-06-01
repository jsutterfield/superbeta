from django.db import models 
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

def save_area(instance, file_name):
    return "photos/%s/%s/%s" % (instance.area.state, instance.area.name, file_name)

def save_problem(instance, file_name):
    return "photos/%s/%s/%s/%s" % (instance.problem.parent.state, instance.problem.parent.name, instance.problem.name, file_name)

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
    name = models.CharField(max_length=100)
    area_type = models.CharField(max_length=2, choices=AREA_CHOICES, 
                help_text="eg 'Bay Area' = Region, 'Indian Rock' = Area, 'Motar Rock' = Boulder")
    area_parent = models.ForeignKey("self", null=True, blank=True)
    state = USStateField()
    city = models.CharField(max_length=20, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    street_address = models.CharField(max_length=40, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    bouldering = models.BooleanField(default=False, blank=True)
    top_rope = models.BooleanField(default=False, blank=True)
    sport = models.BooleanField(default=False, blank=True)
    trad = models.BooleanField(default=False, blank=True)
    approach_difficulty = models.CharField(max_length=12, choices=APPROACH_CHOICES, blank=True)
    approach_time = models.IntegerField(null=True, blank=True, help_text="In minutes")
    approach_distance = models.IntegerField(null=True, blank=True, help_text="In feet (1/4 mi = 1320ft, 1/2 mi = 2640ft, 1 mi = 5280ft)")
    approach_description = models.TextField(blank=True)
    trailhead_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    trailhead_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lot_parking = models.BooleanField(default=False, blank=True)
    street_parking = models.BooleanField(default=False, blank=True)
    garage_parking = models.BooleanField(default=False, blank=True)
    pullout_parking = models.BooleanField(default=False, blank=True)
    parking_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    parking_description = models.CharField(max_length=750, blank=True)
    height = models.IntegerField(null=True, blank=True)
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
    nearest_emergency_phone = PhoneNumberField(null=True, blank=True, help_text='XXX-XXX-XXXX')
    slug = models.SlugField(max_length=50)
    featured = models.BooleanField(default=False)

    def __unicode__(self):
        if self.area_type == 'RE':
            return "%s -- %s" % (self.get_area_type_display(), self.name)
        elif self.area_type == 'AR':
            return "%s -- %s -- %s" % (self.get_area_type_display(), self.name, self.area_parent.name)
        else:
            return "%s -- %s -- %s -- %s" % (self.get_area_type_display(), self.name, self.area_parent.name, 
                                             self.area_parent.area_parent.name)

    def get_absolute_url(self):
        if self.area_type == 'RE':
            return "climbs/%s" % (self.slug)
        elif self.area_type == 'AR':
            return "climbs/%s/%s" % (self.area_parent.slug, self.slug)
        else:
            return "climbs/%s/%s/%s" % (self.area_parent.area_parent.slug,
                                        self.area_parent.slug,
                                        self.slug)

    
class Problem(models.Model):
    PROBLEM_QUALITY = (
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
    quality = models.CharField(max_length=1, choices=PROBLEM_QUALITY, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    description = models.TextField(blank=True)
    height = models.CharField(max_length=20, blank=True)
    angle = models.CharField(max_length=1, choices=ANGLE_CHOICES, blank=True)
    features = models.CharField(max_length=40, blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    problem_start = models.CharField(max_length=100, blank=True)
    problem_descent = models.CharField(max_length=100, blank=True)
    landing_information = models.CharField(max_length=100, blank=True)
    hazard_information = models.CharField(max_length=100, blank=True)
    aspect = models.CharField(max_length=50, blank=True)
    variations = models.CharField(max_length=100, blank=True)
    misc_information = models.CharField(max_length=100, blank=True)
    first_ascent = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=50, help_text='Used in URL to map to database to this route')

    def __unicode__(self):
        return "%s -- %s -- %s -- %s" % (self.name, self.parent.name,
                                         self.parent.area_parent.name, self.parent.state)

    def get_absolute_url(self):
        return "/climbs/%s/%s/%s/%s" % (self.parent.area_parent.area_parent.slug,
                                        self.parent.area_parent.slug, 
                                        self.parent.slug, self.slug)

    def validate_rating(self):
        pass


class ProblemPhoto(models.Model):
    PHOTO_CHOICES = (
        ("O", "Overview"),
        ("G", "General")
    )
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    problem = models.ForeignKey('Problem')
    photo = models.ImageField(upload_to=save_problem)

    def __unicode__(self):
        return "%s-%s" % (self.problem, self.photo_type)

    def get_problem_url(self):
        return self.problem.get_absolute_url()


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

    def get_area_url(self):
        return self.area.get_absolute_url()
