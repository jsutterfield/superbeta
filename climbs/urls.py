from django.conf.urls import patterns, include, url

urlpatterns = patterns('climbs.views',
    url(r'(?P<slug>.*)/$', 'show_route'),
    
)
