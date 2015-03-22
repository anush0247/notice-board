from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.shortcuts import render

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "rid"
    template_name = "users/user_profile.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        #Profile.objects.get_or_create(user=user)
        return user

from auth.models import RUser

def DeptView(request):
    context = {'depts' : RUser.department_labels }
    return render(request, "users/depts.html", context)

def DeptDetailView(request, slug):
    return render(request, "users/dept_details.html")
