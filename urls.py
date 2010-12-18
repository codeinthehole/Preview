from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', include('main.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^permissions/', include('object_permissions.urls')),
    url(r'^$', redirect_to, {'url': '/projects/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', 
            {'document_root': settings.MEDIA_ROOT}),
    )
