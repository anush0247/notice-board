from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import JSONRenderer

from auth.models import RidUser
from users.models import *

router = routers.DefaultRouter()

class BasicInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RidUser
        fields = ('rid','first_name','last_name','gender','date_of_birth')

class BasicInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BasicInfoSerializer
    queryset = RidUser.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
	   return RidUser.objects.filter(rid=self.request.user.rid)

router.register(r'basic_info', BasicInfoViewSet)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RidUser
        fields = ('rid','dept','batch','year')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = RidUser.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
	   return RidUser.objects.filter(rid=self.request.user.rid)

router.register(r'university_info', UserViewSet)

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','mobile','email','url')

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactSerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
	   return Profile.objects.filter(user=RidUser.get(rid=self.request.user.rid))

router.register(r'contact_info', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
