from main.models import *
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Project)

admin.site.register(Page)

admin.site.register(PageVersion)