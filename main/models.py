from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.client.name)

    def get_absolute_url(self):
        return "/%s/%s/" % (self.client.slug, self.slug)

class Page(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-display_order',)

    def __unicode__(self):
        return "%s (%s / %s)" % (self.name, self.project.client.name, self.project.name) 

    def get_versions(self):
        return self.pageversion_set.all()

class PageVersion(models.Model):
    STATUS_CHOICES = (
        ('Open', 'Under review'),
        ('Appproved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    page = models.ForeignKey(Page)
    number = models.IntegerField(default=1)
    image = models.ImageField(upload_to='designs/%Y/%m/%d')
    status = models.CharField(max_length=32, default='Open', choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return "Version #%d of '%s' (%s / %s)" % (self.number, self.page.name, self.page.project.client.name, self.page.project.name) 
