from main.models import *
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

admin.site.register(Project)
admin.site.register(Page)
admin.site.register(PageVersion)