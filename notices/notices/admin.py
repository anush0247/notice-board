from django.contrib import admin
from .models import Notices, Profile, Roles, RolePermissions

#class NoticesAdmin(admin.ModelAdmin):
#    list_display = ('title','sentat','receiver','sender')
#    list_filter = ('receiver',)

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class NoticesResource(resources.ModelResource):
    class Meta:
        model = Notices
        
class NoticesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title','sentat','receiver','sender')
    list_filter = ('receiver',)
    resource_class = NoticesResource
    pass
    
admin.site.register(Notices, NoticesAdmin)

class RoleResource(resources.ModelResource):
    class Meta:
        model = Roles
        
class RoleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #list_display = ('title',)
    resource_class = RoleResource
    pass
    
admin.site.register(Roles, RoleAdmin)


def abc(resource=None):
    return
        
class ProfileResource(resources.ModelResource):
    
    class Meta:
        model = Profile

        
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('name','user')
    resource_class = ProfileResource
    pass

admin.site.register(Profile, ProfileAdmin)
    
class RolePermissionsResource(resources.ModelResource):
    class Meta:
        model = RolePermissions
        
class RolePermissionsAdmin(ImportExportModelAdmin):
    resource_class = RolePermissionsResource
    pass
    
admin.site.register(RolePermissions, RolePermissionsAdmin)
