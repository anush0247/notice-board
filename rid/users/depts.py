
# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from .views import DeptView
from .views import DeptDetailView
# auth url patterns
urlpatterns = patterns('',
	url(r"^$", auth(DeptView), name="depts"),
        url(r'^(?P<slug>[A-Z]{2,3})/$',auth(DeptDetailView),name="dept_details"),               
)
 

