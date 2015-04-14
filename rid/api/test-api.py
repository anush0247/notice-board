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
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'contact_info', ContactViewSet)

class ProfilePicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','profile_pic')

class ProfilePicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfilePicSerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'profile_pic', ProfilePicViewSet)

class SummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','summary')

class SummaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SummarySerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'summary', SummaryViewSet)

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('user','school','period','degree','stream','grade')

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Education.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'education', EducationViewSet)

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('title',)

class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    renderer_classes = (JSONRenderer, )
     
router.register(r'areas_list', AreaViewSet)

class UserAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','areas')

class UserAreaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserAreaSerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'areas', UserAreaViewSet)


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('title',)

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    renderer_classes = (JSONRenderer, )
     
router.register(r'skill_list', SkillViewSet)

class UserSkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','skills')

class UserSkillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSkillSerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'skills', UserSkillViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
