import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files import File

from main.models import Client, Project, Page, PageVersion


class Command(BaseCommand):
    help = 'Creates a new preview project from a set of images'

    def handle(self, *args, **options):
        """
        Special command for creating a new project from the commandline
        """
        self.write()
        self.write("PREVIEW - New project creator")
        self.write()
        client = self.choose_client()
        project = self.create_project(client)
        self.create_pages(project)

    def create_pages(self, project, prompt="Enter path to image folder: "):
        path_to_images = raw_input(prompt)
        if not os.path.isdir(path_to_images):
            return create_pages(project, "%s is not a valid path - choose again: ")
        
        # Use alphabetically sorted list
        files = os.listdir(path_to_images)
        files.sort(lambda x,y: cmp(x.upper(), y.upper()))
        display_order = 0
        for filename in files:
            # This could be more sophisticated...
            pagename = filename.split(".")[0]
            self.write("Found file %s, creating page with name '%s'" % (filename, pagename))
            # Save page and page version
            page = Page.objects.create(name=pagename, display_order=display_order, project=project)
            display_order += 1
            page_version = PageVersion()
            page_version.page = page
            page_version.image.save(filename, File(open(os.path.join(path_to_images, filename))))
            page_version.save()

    def create_project(self, client):
        # List all current projects for this client to avoid clashes
        projects = client.projects.all()
        self.write("Current projects: %s" % ", ".join([p.name for p in projects]))
        
        project_name = raw_input("Name of new project? ")
        try:
            existing_project = client.projects.get(name=project_name)
            self.write("A project already exists with name '%s'" % project_name)
            return create_project(client)
        except Project.DoesNotExist:
            pass
        project_desc = raw_input("Description (optional)? ")
        
        self.write("    Creating project '%s'" % project_name)
        project = Project()
        project.client = client
        project.name = project_name
        project.description = project_desc
        project.save()
        return project

    def choose_client(self, prompt="a). Choose a client:"):
        self.write(prompt)
        self.write("    [0] <New client>")
        for client in Client.objects.all():
            self.write("    [%d] %s" % (client.pk, client.name))
        client_pk = int(raw_input("Select number: "))

        # Create client object
        if client_pk == 0:
            client_name = raw_input("Name of new client? ")
            self.write("    Creating client '%s'" % client_name)
            client = Client.objects.create(name=client_name)
        else:
            try:
                client = Client.objects.get(pk=client_pk)
            except Client.DoesNotExist:
                return self.choose_client("%d is not a valid option - choose again:" % client_pk)
        return client

    def write(self, output=""):
        self.stdout.write(output+"\n")

        