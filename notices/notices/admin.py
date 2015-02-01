from django.contrib import admin
from .models import Notices

class NoticesAdmin(admin.ModelAdmin):
    list_display = ('title','sentat','receiver','sender')
    list_filter = ('receiver',)

admin.site.register(Notices, NoticesAdmin)
