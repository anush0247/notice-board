# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.edit_views import UpdateProfilePic, UpdateContactInfo, EducationListView, UpdateSkills, AddSkill
from users.edit_views import AddArea, UpdateAreas, UpdateEducation, AddEducation
# auth url patterns
urlpatterns = patterns('',
    url(r"^contact_info/$", auth(UpdateContactInfo.as_view()), name="edit_contact_info"),
    url(r"^profile_pic/$", auth(UpdateProfilePic.as_view()), name="edit_profile_pic"),
    url(r"^education/$", auth(EducationListView.as_view()), name="education_list"),
    url(r"^education/add$", auth(AddEducation.as_view()), name="education_add"),
    url(r"^education/(?P<pk>[0-9]+)/update$", auth(UpdateEducation.as_view()), name="education_update"),
    url(r"^skills/$", auth(UpdateSkills.as_view()), name="edit_skills"),
    url(r"^skills/add$", auth(AddSkill.as_view()), name="skill_add"),
    url(r"^areas/$", auth(UpdateAreas.as_view()), name="edit_areas"),
    url(r"^areas/add$", auth(AddArea.as_view()), name="area_add"),
)
 

