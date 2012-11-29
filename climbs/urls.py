from django.conf.urls import patterns, include, url

urlpatterns = patterns('routes.views',
    url(r'(?P<slug>.*)/$', 'show_route'),
    url(r'test$/', 'shamus'),
)
