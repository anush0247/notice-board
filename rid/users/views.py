from django.contrib.auth import get_user_model
from django.views.generic import DetailView
# Create your views here.

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "rid"
    template_name = "users/user_profile.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        #Profile.objects.get_or_create(user=user)
        return user


