from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin
admin.autodiscover()

from .views import NoticesView
from .views import HomePageView

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', auth(HomePageView), name="home"),
                       url(r'^notices/$', auth(NoticesView.as_view()), name="notices"),
                       url(r"^login/$", "django.contrib.auth.views.login",
                           {"template_name": "login2.html"}, name="login"),
                       url(r"^logout/$", "django.contrib.auth.views.logout_then_login",
                           name="logout"),
)
