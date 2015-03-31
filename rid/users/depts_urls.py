# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth

from users.depts_views import DeptDetailView, DeptView

# auth url patterns
urlpatterns = patterns('',
	url(r"^$", auth(DeptView), name="depts"),
        url(r'^([A-Z]{2,3})/$', auth(DeptDetailView.as_view()), name="single_dept"),
        url(r'^([A-Z]{2,3})/([A-Z1-4]{2})$', auth(DeptDetailView.as_view()), name="single_dept_filter"),
)
 

