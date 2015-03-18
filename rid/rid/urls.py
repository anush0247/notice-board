from django.conf.urls import patterns, include, url

# importing settings config
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^auth/', include('auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
        urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
        
