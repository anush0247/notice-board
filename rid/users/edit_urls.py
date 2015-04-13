# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.edit_views import UpdateProfilePic, UpdateContactInfo, EducationListView, UpdateSkills, AddSkill
from users.edit_views import AddArea, UpdateAreas, UpdateEducation, AddEducation, DelEducation
from users.edit_views import UserRoleListView, AddUserRole, UpdateUserRole, DelUserRole, AddRole, AddRolePermission
# auth url patterns
urlpatterns = patterns('',
    url(r"^contact_info/$", auth(UpdateContactInfo.as_view()), name="edit_contact_info"),
    url(r"^profile_pic/$", auth(UpdateProfilePic.as_view()), name="edit_profile_pic"),
    url(r"^education/$", auth(EducationListView.as_view()), name="education_list"),
    url(r"^education/add$", auth(AddEducation.as_view()), name="education_add"),
    url(r"^education/(?P<pk>[0-9]+)/update$", auth(UpdateEducation.as_view()), name="education_update"),
    url(r"^education/(?P<pk>[0-9]+)/delete$", auth(DelEducation.as_view()), name="education_del"),
    url(r"^skills/$", auth(UpdateSkills.as_view()), name="edit_skills"),
    url(r"^skills/add$", auth(AddSkill.as_view()), name="skill_add"),
    url(r"^areas/$", auth(UpdateAreas.as_view()), name="edit_areas"),
    url(r"^areas/add$", auth(AddArea.as_view()), name="area_add"),
    url(r"^roles/$", auth(UserRoleListView.as_view()), name="user_role_list"),
    url(r"^roles/add$", auth(AddUserRole.as_view()), name="user_role_add"),
    url(r"^roles/add/new_role/$", auth(AddRole.as_view()), name="role_add"),
    url(r"^roles/add/new_role_permission/$", auth(AddRolePermission.as_view()), name="role_permission_add"),
    url(r"^roles/(?P<pk>[0-9]+)/update$", auth(UpdateUserRole.as_view()), name="user_role_update"),
    url(r"^roles/(?P<pk>[0-9]+)/delete$", auth(DelUserRole.as_view()), name="user_role_del"),

)
 

