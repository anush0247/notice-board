from django.core.urlresolvers import reverse
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied
from django.contrib import messages


from users.models import Profile
from users.edit_forms import ProfilePicForm, ContactInfoForm


class UpdateProfilePic(UpdateView):
    model = Profile
    template_name = "users/edit/profile_pic.html"
    form_class = ProfilePicForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Profile Pic Updated successfully')
        return reverse('edit_profile_pic', kwargs={'slug':self.object.user})

class UpdateContactInfo(UpdateView):
    model = Profile
    template_name = "users/edit/contact_info.html"
    form_class = ContactInfoForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Contact Info Updated successfully')
        return reverse('edit_contact_info', kwargs={'slug':self.object.user})
