from django.conf.urls.defaults import *

urlpatterns = patterns('main.views',
    url(r'(?P<client_slug>[\w-]*)/(?P<project_slug>[\w-]*)/$', 'project',
            name='main-project'),
    url(r'(?P<client_slug>[\w-]*)/$', 'client',
            name='client-projects'),
)
