# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from .views import DevIntro

# auth url patterns
urlpatterns = patterns('',
    url(r"^intro/$", DevIntro, name="dev_into"),
)
 
