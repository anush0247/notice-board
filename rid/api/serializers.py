from django.forms import widgets
from rest_framework import serializers
from users.models import *
from auth.models import RidUser
from rest_framework import permissions

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class RidUserSerializer(serializers.ModelSerializer):

	class Meta:
		permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
		model=RidUser
		fields=('rid','first_name','last_name','date_of_birth','gender')

class UniversitySerializer(serializers.ModelSerializer):

	class Meta:
		model=RidUser
		fields=('rid','dept','batch','year')

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields=('mobile','url','email')


class ProfilePicSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
	    model = Profile
	    fields=('profile_pic',)


class SummarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields=('summary',)

class EducationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Education
		fields=('period','degree','stream','grade','school')
		dept = 2

class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields=('title',)

class ProfileAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields=('areas',)
        depth = 2


class UserRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserRole
        fields=('role','is_verified')
        depth = 3

class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields=('title',)

class ProfileSkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields=('skills',)
        depth = 2

class AchievementSerializer(serializers.ModelSerializer):

	class Meta:
		model = Achievement
		fields=('issuer','title','location','period','description')


class ExperienceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Experience
		fields=('organization','title','location','period','description')
