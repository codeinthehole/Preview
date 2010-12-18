from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from object_permissions import register

class Client(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Client, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('main-client', [self.slug])

register(['view','comment','approve'], Client)

class Project(models.Model):
    client = models.ForeignKey('main.Client', related_name="projects")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.client.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('main-client-project', [self.client.slug, self.slug])


class Page(models.Model):
    project = models.ForeignKey('main.Project', related_name="pages")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, null=True, unique=True)
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-display_order',)

    def __unicode__(self):
        return u"%s (%s / %s)" % (self.name, self.project.client.name,
                                        self.project.name)
       
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)    
        
    @models.permalink
    def get_absolute_url(self):
        return ('main-client-project-page', [self.client.slug, self.slug])


class PageVersion(models.Model):
    OPEN, APPROVED, REJECTED = range(1, 4)
    STATUS_CHOICES = (
        (OPEN, _("Under review")),
        (APPROVED, _("Approved")),
        (REJECTED, _("Rejected")),
    )
    page = models.ForeignKey('main.Page', related_name="versions")
    number = models.IntegerField(default=1)
    image = models.ImageField(upload_to='designs/%Y/%m/%d')
    status = models.IntegerField(default=OPEN, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="created_pageversions", null=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(User, null=True, blank=True, 
            related_name="approved_pageversions")

    def __unicode__(self):
        return u"Version #%d of '%s' (%s / %s)" % (self.number, 
                                                   self.page.name, 
                                                   self.page.project.client.name, 
                                                   self.page.project.name)
