from django.conf.urls import patterns, include, url

urlpatterns = patterns('climbs.views',
    (r'^(?P<region_slug>[\w_-]+)/$', 'region'),
    (r'^(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/$', 'area'),
    (r'^(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/(?P<boulder_slug>[\w_-]+)/$', 'boulder'),
    (r'^(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/(?P<boulder_slug>[\w_-]+)/(?P<problem_slug>[\w_-]+)/$', 'problem'),   
)