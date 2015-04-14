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

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RidUser
        fields = ('rid','first_name','last_name','gender','date_of_birth','dept','batch','year')

class UserInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = RidUser.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
	   return RidUser.objects.filter(rid=self.request.user.rid)

router.register(r'user_info', UserInfoViewSet)

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


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ('user','issuer','title','location','period','description')

class AchievementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AchievementSerializer
    queryset = Achievement.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Achievement.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'achievements', AchievementViewSet)


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = ('user','organization','title','location','period','description')

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Experience.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'experiences', ExperienceViewSet)

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

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','mobile','url','email','profile_pic','summary','areas','skills')

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return Profile.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'profile_info', UserProfileViewSet)

class RolePermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RolePermission
        fields = ('title','is_verified')

class RolePermissionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RolePermissionSerializer
    queryset = RolePermission.objects.all()
    renderer_classes = (JSONRenderer, )
     
router.register(r'role_permission_list', RolePermissionViewSet)

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('title','permissions','is_verified')

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    renderer_classes = (JSONRenderer, )
     
router.register(r'role_list', RoleViewSet)

class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRole
        fields = ('user','role','is_verified')

class UserRoleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()
    renderer_classes = (JSONRenderer, )
    def get_queryset(self):
        return UserRole.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid))

router.register(r'roles', UserRoleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
