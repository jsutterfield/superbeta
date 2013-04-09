from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'superbeta.views.home'),
    (r'^climbs/', include('superbeta.climbs.urls')),
    # (r'^climbs/(?P<region_slug>[\w_-]+)/$', 'superbeta.views.region'),
    # (r'^climbs/(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/$', 'superbeta.views.area'),
    # (r'^climbs/(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/(?P<boulder_slug>[\w_-]+)/$', 'superbeta.views.boulder'),
    # (r'^climbs/(?P<region_slug>[\w_-]+)/(?P<area_slug>[\w_-]+)/(?P<boulder_slug>[\w_-]+)/(?P<route_slug>[\w_-]+)/$', 'superbeta.views.route'),
    
    # url(r'^superbeta/', include('superbeta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
