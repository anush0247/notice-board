# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from .views import DevDoc

# auth url patterns
urlpatterns = patterns('',
    url(r"^docs/$", DevDoc, name="dev_doc"),
)
 
