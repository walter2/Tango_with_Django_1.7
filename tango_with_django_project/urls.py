from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango import views

'''Tango with Django project URL pattern filters.'''

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )