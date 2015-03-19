
# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from .views import UserProfileDetailView

# auth url patterns
urlpatterns = patterns('',
                       url(r"^(?P<slug>[A-Za-z0-9_]+)/$", auth(UserProfileDetailView.as_view()), name="profile"),
)
 

