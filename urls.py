from django.conf import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
