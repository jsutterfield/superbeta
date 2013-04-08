# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from climbs.models import Route
# from django.conf import settings


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     favorites = models.ManyToManyField(Route, related_name="user_favorites", blank=True, null=True)
#     projects = models.ManyToManyField(Route, related_name="user_projects",  blank=True, null=True)
#     DEFAULT_AVATAR = settings.STATIC_URL + "default-avatar.png"
#     avatar = models.ImageField(upload_to="avatars", default=DEFAULT_AVATAR)

#     def __unicode__(self):
#         return self.user.username


# class Send(models.Model):
    
#     SEND_TYPE_OPTIONS = (
#         ("O", "On-sight Flash"),
#         ("F", "Flash"),
#     )

#     route = models.ForeignKey(Route)
#     user = models.ForeignKey(User)
#     date_sent = models.DateField(null=True, blank=True)
#     send_type = models.CharField(max_length=1, choices=SEND_TYPE_OPTIONS, blank=True)

#     def __unicode__(self):
#         return "%s -- %s" % (self.user.username, self.route.name)


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)