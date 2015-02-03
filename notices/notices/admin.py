from django.contrib import admin
from .models import Notices, Profile, Roles, RolePermissions

class NoticesAdmin(admin.ModelAdmin):
    list_display = ('title','sentat','receiver','sender')
    list_filter = ('receiver',)

admin.site.register(Notices, NoticesAdmin)
admin.site.register(Roles)
admin.site.register(Profile)
admin.site.register(RolePermissions)
