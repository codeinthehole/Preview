from django.conf.urls.defaults import *
from django.views.generic import simple
from main.models import Client 

urlpatterns = patterns('main.views',
    url(r'(?P<client_slug>[\w-]*)/(?P<project_slug>[\w-]*)/(?P<page_slug>[\w-]*)/(?P<version_no>[\d]*)/$', 'page_version_comments',
            name='comments-page-project'),
    url(r'(?P<client_slug>[\w-]*)/(?P<project_slug>[\w-]*)/$', 'project',
            name='main-project'),
    url(r'(?P<client_slug>[\w-]*)/$', 'client',
            name='client-projects'),
    url(r'^$', simple.direct_to_template, {'template': 'main/clients.html'}, name='all-clients'),
)
