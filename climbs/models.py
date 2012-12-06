from django.db import models 
from autoslug import AutoSlugField

STAR_RATING = (
    # Look into having the first value be nums, not strings.
    ('1', "One Star"),
    ('2', "Two Star"),
    ('3', "Three Star"),
    ('4', "Four Star"),
)

    
class Route(models.Model):

    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weather = models.TextField(blank=True)
    history = models.TextField(blank=True)
    area = models.ForeignKey('Area')
    slug = AutoSlugField(populate_from='name', unique_with='area__name')


    def __unicode__(self):
        return self.name

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


class Area(models.Model):

    APPROACH_CHOICES = (
        ("Easy", "Flip Flops"),
        ("Intermediate", "Sneakers"),
        ("Difficult", "Boots")
    )

    name = models.CharField(max_length=100)
    # Should we allow area to have the same name if in different States?
    slug = AutoSlugField(populate_from='name', unique=True)
    about = models.TextField(blank=True)
    parking_desc = models.TextField(blank=True)
    parking_gps = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    approach_desc = models.TextField(blank=True)
    approach_rating = models.CharField(max_length=15, choices=APPROACH_CHOICES,
                                       blank=True)
    approach_length = models.TextField(blank=True)
    misc = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class AreaPhoto(models.Model):

    PHOTO_CHOICES = (
        ("G", "General"),
        ("A", "Approach"),
    )
    
    # Figure out a better naming scheme for where the photos
    # are uploaded to
    photo = models.ImageField(upload_to="photos")
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    area = models.ForeignKey('Area')
    # Look into changing this field - chartype doesn't seem right
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)

    def __unicode__(self):
        return "%s-%s" % (self.area, self.photo_type)