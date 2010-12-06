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


class PageVersionAdmin(admin.ModelAdmin):
    """This sets up the admin to automatically add the creator user"""
    
    exclude = ('created_by', 'approved_by', 'approval_date')
    
    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        if not hasattr(instance, 'created_by'):
            instance.created_by = request.user
        instance.save()
        form.save_m2m()
        return instance
    
    def save_formset(self, request, form, formset, change): 

        def set_user(instance):
            if not instance.created_by:
                instance.created_by = request.user
            instance.save()

        if formset.model == PageVersion:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

admin.site.register(PageVersion, PageVersionAdmin)