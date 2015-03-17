from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin

from .views import NoticesView, OneNoticeView, HomePageView, AddNotice, UpdateNotice, DelNotice, UserProfileDetailView
from .api import UserViewSet, ProfileViewSet, RoleViewSet, RolePermissionsViewSet, GroupViewSet
from rest_framework import routers

from .views import ApiEndpoint
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet, base_name="")
router.register(r'users', UserViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'roles', RoleViewSet)                                        
router.register(r'permissions', RolePermissionsViewSet)

urlpatterns = patterns('',
    url(r'^dj-admin/', include(admin.site.urls)),
    url(r'^dj-admin/docs/', include("django.contrib.admindocs.urls")),
    url(r'^$', auth(HomePageView), name="home"),
    url(r'^notices/$', auth(NoticesView.as_view()), name="notices"),
    url(r'^notices/(E[234]){1}/$', auth(NoticesView.as_view()), name="notices_year"),
    url(r"^notices/(?P<pk>\d+)$", auth(OneNoticeView.as_view()), name="notice_detail"),
    url(r"^notices/add/$", auth(AddNotice.as_view()), name="notice_add"),
    url(r"^notices/(?P<pk>\d+)/(?P<action>update)/$", auth(UpdateNotice.as_view()), name="notice_update"),
    url(r"^notices/(?P<pk>\d+)/(?P<action>delete)/$", auth(DelNotice.as_view()), name="notice_delete"),
    url(r"^login/$", "django.contrib.auth.views.login", {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login", name="logout"),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include(router.urls)),
    url(r"^users/(?P<slug>[\w .]+)/$", auth(UserProfileDetailView.as_view()), name="profile"),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/hello', ApiEndpoint.as_view()),
    url(r'^secret$', 'notices.views.secret_page', name='secret'),
)

if settings.DEBUG:
    urlpatterns += patterns('',url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
                            
