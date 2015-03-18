from django.conf.urls import patterns, include, url

# importing settings config
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# importing home page view
from rid.views import HomePageView

urlpatterns = patterns('',
	url(r'^$', HomePageView, name="home"),
	url(r'^auth/', include('auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
        urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
        
