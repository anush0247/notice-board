from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from auth.models import RidUser, Profile, Roles, RolePermission, Skill, Area, Education, Experience, Achievement, UserRole


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = RidUser
        fields = ('rid','date_of_birth','gender','first_name','dept','year')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = RidUser
        fields = ('rid','first_name','last_name','date_of_birth','gender','dept','batch','year','is_active', 'is_admin')
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('rid','first_name','gender', 'date_of_birth','dept','batch','year','is_admin')
    list_filter = ('dept','gender','year')
    fieldsets = (
        ('User Info', {'fields': ('rid','first_name','last_name')}),
        ('Security',{'fields': ('password',)}),
        ('Basic Personal Info', {'fields': ('date_of_birth','gender')}),
        ('University Info',{'fields': ('dept','batch','year')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    
    add_fieldsets = (
        ('User Info', {'fields': ('rid','first_name','last_name',)}),
        ('Security',{'fields': ('password1','password2')}),
        ('Basic Personal Info', {'fields': ('date_of_birth','gender')}),
        ('University Info',{'fields': ('dept','batch','year')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('rid','first_name','last_name')
    ordering = ('rid',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(RidUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(Area, AreaAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Skill, SkillAdmin)

class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(RolePermission, RolePermissionAdmin)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('permissions',)

admin.site.register(Roles, RolesAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('user','mobile','email','url',)
    filter_horizontal = ('roles','Area','Skill',)

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
