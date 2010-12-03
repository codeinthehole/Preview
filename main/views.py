from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings

from main.models import *

def project(request, client_slug, project_slug):

    client = get_object_or_404(Client, slug=client_slug)
    project = get_object_or_404(Project, slug=project_slug)
    if project.client != client:
        raise Http404
    pages = Page.objects.filter(project=project)

    return render_to_response('project.html', {'pages': pages})
