from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied


from users.models import Profile
from users.edit_forms import ProfilePicForm


class UpdateProfilePic(UpdateView):
    model = Profile
    template_name = "users/edit/profile_pic.html"
    form_class = ProfilePicForm
   
    #def __init__(self, **kwargs):
	
	
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        #messages.success(self.request,'Notice #'+str(self.object.pk)+' updated successfully')
        return reverse('edit_profile_pic', kwargs={'slug':self.object.user})


