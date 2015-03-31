from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required as auth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from users.models import *
from auth.models import RidUser
from api.serializers import *

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content = JSONRenderer().render(data,renderer_context={'indent':4})
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

@auth
def basic(request):
    try:
        basic_info = RidUser.objects.get(rid=request.user.rid)
    except RidUser.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = RidUserSerializer(basic_info)
        return JSONResponse(serializer.data)

@auth
def university_info(request):
    try:
        university_info = RidUser.objects.get(rid=request.user.rid)
    except RidUser.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = UniversitySerializer(university_info)
        return JSONResponse(serializer.data)
    
@auth
def contact_info(request):
    try:
        contact_info = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ContactSerializer(contact_info)
        return JSONResponse(serializer.data)


@auth
def profile_pic(request):
    try:
        profile_pic = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ProfilePicSerializer(profile_pic)
        return JSONResponse(serializer.data)


@auth
def summary(request):
    try:
        summary = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SummarySerializer(summary)
        return JSONResponse(serializer.data)

@auth
def education(request):
    try:
        education = Education.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Education.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EducationSerializer(education)
        return JSONResponse(serializer.data)

@auth
def area(request):
    try:
        area = Profile.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileAreaSerializer(area)
        return JSONResponse(serializer.data)

@auth
def roles(request):
    try:
        roles = UserRole.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except UserRole.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserRoleSerializer(roles)
        return JSONResponse(serializer.data)

@auth
def skills(request):
    try:
        skills = Profile.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSkillSerializer(skills)
        return JSONResponse(serializer.data)

@auth
def achievements(request):
    try:
        achievement = Achievement.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Achievement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AchievementSerializer(achievement)
        return JSONResponse(serializer.data)

@auth
def experiences(request):
    try:
        experience = Experience.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Experience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperienceSerializer(experience)
        return JSONResponse(serializer.data)