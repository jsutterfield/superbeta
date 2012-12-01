from django.db import models 

STAR_RATING = (
    # Look into having the first value be nums, not strings.
    ('1', "One Star"),
    ('2', "Two Star"),
    ('3', "Three Star"),
    ('4', "Four Star"),
)
    
class Route(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    difficulty = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)
    height = models.IntegerField(null=True)
    weather = models.TextField(blank=True)
    history = models.TextField(blank=True)


    def __unicode__(self):
        return self.name

    def validate_rating(self):
        pass

class Photo(models.Model):

    PHOTO_CHOICES = (
        ("T", "Topo"),
        ("B", "Beta"),
        ("C", "Context"),
        ("G", "Genera")
    )
    
    # Figure out a better naming scheme for where the photos
    # are uploaded to
    photo = models.ImageField(upload_to="photos")
    photo_type = models.CharField(max_length=1, choices=PHOTO_CHOICES)
    route = models.ForeignKey('Route')
    # Look into changing this field - chartype doesn't seem right
    quality_rating = models.CharField(max_length=1, choices=STAR_RATING, blank=True)

    def __unicode__(self):
        return "%s-%s" % (self.route, self.photo_type)
