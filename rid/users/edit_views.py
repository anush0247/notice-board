from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

from users.models import Profile
from users.edit_forms import ProfilePicForm


class UpdateProfilePic(UpdateView):
    model = Profile
    template_name = "users/edit/profile_pic.html"
    form_class = ProfilePicForm
   
    def get_object(self, queryset=None):
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        #messages.success(self.request,'Notice #'+str(self.object.pk)+' updated successfully')
        return reverse('edit_profile_pic', kwargs={'slug':self.object.user})

    #def get_context_data(self, **kwargs):
    #    context = super(UpdateProfilePic, self).get_context_data(**kwargs)
	#context['form'] = ProfilePicForm()
	#return context
