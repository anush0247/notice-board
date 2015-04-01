# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.edit_views import UpdateProfilePic
 
# auth url patterns
urlpatterns = patterns('',
    url(r"^profile_pic/$", auth(UpdateProfilePic.as_view()), name="edit_profile_pic"),
)
 

