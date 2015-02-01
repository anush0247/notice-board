from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import NoticesView
from .views import HomePageView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView, name="home"),
    url(r'^notices/$', NoticesView.as_view(), name="notices"),
)
