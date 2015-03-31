from django.contrib import admin
from users.models import Profile, Role, RolePermission, Skill, Area, Education, Experience, Achievement, UserRole

class AreaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Area, AreaAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Skill, SkillAdmin)

class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('title','is_verified')

admin.site.register(RolePermission, RolePermissionAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('title','is_verified')
    filter_horizontal = ('permissions',)

admin.site.register(Role, RoleAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('user','mobile','email','url',)
    filter_horizontal = ('areas','skills',)

admin.site.register(Profile, ProfileAdmin)

class UserRoleAdmin(admin.ModelAdmin):
    list_display= ('user','role','is_verified')

admin.site.register(UserRole, UserRoleAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display=('user','school','degree','period',)

admin.site.register(Education, EducationAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display=('user','organization','title','period',)

admin.site.register(Experience, ExperienceAdmin)

class AchievementAdmin(admin.ModelAdmin):
    list_display=('user','title','issuer',)

admin.site.register(Achievement, AchievementAdmin)
