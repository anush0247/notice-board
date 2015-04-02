# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.edit_views import UpdateProfilePic, UpdateContactInfo, EducationListView, UpdateSkills
 
# auth url patterns
urlpatterns = patterns('',
    url(r"^contact_info/$", auth(UpdateContactInfo.as_view()), name="edit_contact_info"),
    url(r"^profile_pic/$", auth(UpdateProfilePic.as_view()), name="edit_profile_pic"),
    url(r"^education/$", auth(EducationListView.as_view()), name="education_list"),
    url(r"^skills/$", auth(UpdateSkills.as_view()), name="edit_skills"),
)
 

