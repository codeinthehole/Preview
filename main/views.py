from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from main.models import *

@login_required
def project(request, client_slug, project_slug):
    """Show versions for a project"""
    client = get_object_or_404(Client, slug=client_slug)
    if not request.user.has_perm('view', client):
	return HttpResponseForbidden("You are not allowed to see projects")
    project = get_object_or_404(Project, slug=project_slug)
    if project.client != client:
        raise Http404
    pages = Page.objects.filter(project=project)

    return render_to_response('main/project.html', {
        'pages': pages,
        'client': client,
        'project': project,}, context_instance=RequestContext(request))

@login_required
def page(request, client_slug, project_slug, page_slug):
    client = get_object_or_404(Client, slug=client_slug)
    if not request.user.has_perm("view", client):
	return HttpResponseForbidden("You are not allowed to see this page")
    project = get_object_or_404(Project, slug=project_slug)
    page = get_object_or_404(Page, slug=page_slug)
    if project.client != client and page.project != project:
        raise Http404
    return render_to_response('main/page.html', locals(),
            context_instance=RequestContext(request))

@login_required
def page_version_comments(request, client_slug, project_slug, page_slug, version_no):
    """Show comments for a version of a page"""
    client = get_object_or_404(Client, slug=client_slug)
    if not request.user.has_perm(["view", "comment"], client):
	return HttpResponseForbidden("You are not allowed to see page comments")
    project = get_object_or_404(Project, slug=project_slug)
    page = get_object_or_404(Page, slug=page_slug)
    if project.client != client and page.project != project:
        raise Http404
    page_version = get_object_or_404(PageVersion, page=page, number=version_no)
    next = reverse(page_version_comments, args=[client.slug, project.slug, page.slug, page_version.number])
    return render_to_response('main/page_comments.html', locals(),
            context_instance=RequestContext(request))

@login_required
def client(request, client_slug):
    """Shows all projects that belong to a client"""
    return render_to_response('main/client.html', {
        'client': get_object_or_404(Client, slug=client_slug)
        }, context_instance=RequestContext(request))
    


