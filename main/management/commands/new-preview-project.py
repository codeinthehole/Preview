from django.core.management.base import BaseCommand, CommandError
from main.models import Client, Project

class Command(BaseCommand):
    help = 'Creates a new preview project from a set of images'

    def handle(self, *args, **options):
        """
        Special command for creating a new project
        """
        self.write()
        self.write("PREVIEW - New project creator")
        self.write()
        client = self.choose_client()
        project = self.create_project(client)
        self.create_pages(project)

    def create_pages(self, project):
        path_to_images = raw_input("Enter path to image folder:")

    def create_project(self, client):
        project_name = raw_input("Name of new project? ")
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

        