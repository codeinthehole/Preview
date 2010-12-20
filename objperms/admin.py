from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline
from main.models import Client
from main.admin import ClientAdmin as OldClientAdmin

from objperms.models import ObjectPermission

class ObjectPermissionInline(GenericTabularInline):
    model = ObjectPermission
    raw_id_fields = ['user']

class ObjectPermissionMixin(object):
    def has_change_permission(self, request, obj=None):
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' + opts.get_change_permission(), obj)

    def has_delete_permission(self, request, obj=None):
        opts = self.opts
        return request.user.has_perm(opts.app_label + '.' + opts.get_delete_permission(), obj)

class ClientAdmin(ObjectPermissionMixin, OldClientAdmin):
    inlines = OldClientAdmin.inlines + [ObjectPermissionInline]

admin.site.unregister(Client)
admin.site.register(Client, ClientAdmin)