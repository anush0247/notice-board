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
        url(r'^api/v1/', include('api.urls')),
        url(r'^api/v2/', include('api.test-api')),
        url(r'^users/', include('users.urls')),
        url(r'^depts/', include('users.depts_urls')),
        url(r'^dev/', include('dev.urls')),
        url(r'^admin/', include(admin.site.urls)),
	url(r'^dev/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)

if settings.DEBUG:
        urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
        
