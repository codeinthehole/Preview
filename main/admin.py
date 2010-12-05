from main.models import *
from django.contrib import admin

class ClientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Project)

class PageAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js', 
            'js/admin-list-reorder.js',
        )
    list_display = ['name', 'display_order']
    list_editable = ['display_order']
    readonly_fields = ['display_order']
admin.site.register(Page, PageAdmin)

admin.site.register(PageVersion)