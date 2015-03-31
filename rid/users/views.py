from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView
from django.shortcuts import render

from users.models import Profile, Education, Experience, Achievement, UserRole
from auth.models import RidUser

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "rid"
    template_name = "users/user_profile.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        Profile.objects.get_or_create(user=user)
        return user

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
	context['roles']   = UserRole.objects.filter(user=RidUser.objects.filter(rid=str(self.kwargs['slug'])))
        context['education']   = Education.objects.filter(user=RidUser.objects.filter(rid=str(self.kwargs['slug'])))
        context['experience']   = Experience.objects.filter(user=RidUser.objects.filter(rid=str(self.kwargs['slug'])))
        context['achievements']   = Achievement.objects.filter(user=RidUser.objects.filter(rid=str(self.kwargs['slug'])))        
        
        return context
