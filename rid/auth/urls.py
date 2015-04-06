# importing django url patterns modules
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from .views import PasswordChangeView

# auth url patterns
urlpatterns = patterns('',
    url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "auth/login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),
    url(r'^settings/change_password/$',auth(PasswordChangeView.as_view()) , name="change_password"),
)
 
