from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required as auth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt
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
@csrf_exempt
def basic(request):
    try:
        basic_info = RidUser.objects.get(rid=request.user.rid)
    except RidUser.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        serializer = RidUserSerializer(basic_info)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def university_info(request):
    try:
        university_info = RidUser.objects.get(rid=request.user.rid)
    except RidUser.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        serializer = UniversitySerializer(university_info)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)
    
@auth
@csrf_exempt
def contact_info(request):
    try:
        contact_info = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        serializer = ContactSerializer(contact_info)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)


@auth
@csrf_exempt
def profile_pic(request):
    #print 'hello'
    try:
        profile_pic = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
        print profile_pic
    except Profile.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'POST':
        serializer = ProfilePicSerializer(profile_pic)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)


@auth
@csrf_exempt
def summary(request):
    try:
        summary = Profile.objects.get(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = SummarySerializer(summary)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def education(request):
    try:
        education = Education.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Education.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = EducationSerializer(education)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def areas(request):
    try:
        area = Profile.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = ProfileAreaSerializer(area)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def roles(request):
    try:
        roles = UserRole.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except UserRole.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = UserRoleSerializer(roles)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def skills(request):
    try:
        skills = Profile.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = ProfileSkillSerializer(skills)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def achievements(request):
    try:
        achievement = Achievement.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Achievement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = AchievementSerializer(achievement)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)

@auth
@csrf_exempt
def experiences(request):
    try:
        experience = Experience.objects.filter(user=RidUser.objects.get(rid=request.user.rid))
    except Experience.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = ExperienceSerializer(experience)
        return JSONResponse(serializer.data)
    else:
	return HttpResponse(status=403)
