# importing django url patterns modules
from django.conf.urls import patterns, include, url

# auth url patterns
urlpatterns = patterns('',
    url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),
)
 
