from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib import messages


from users.models import Profile, Education, Skill, Area, Role, RolePermission, UserRole
from auth.models import RidUser
from users.edit_forms import ProfilePicForm, ContactInfoForm, SkillsForm, AddSkillForm
from users.edit_forms import AreasForm, AddAreaForm, EducationForm
from users.edit_forms import UserRoleForm, AddRoleForm, AddRolePermissionForm

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

class UpdateSkills(UpdateView):
    model = Profile
    template_name = "users/edit/skills.html"
    form_class = SkillsForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Skills Updated successfully')
        return reverse('edit_skills', kwargs={'slug':self.object.user})
        
class AddSkill(CreateView):
    model = Skill
    form_class = AddSkillForm
    template_name = "users/edit/skill_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Skill added successfully')
        return super(AddSkill, self).form_valid(form)

    def get_success_url(self):
        return reverse('edit_skills', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass


class UpdateAreas(UpdateView):
    model = Area
    template_name = "users/edit/areas.html"
    form_class = AreasForm
   
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        return Profile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        messages.success(self.request,'Areas Updated successfully')
        return reverse('edit_areas', kwargs={'slug':self.object.user})

class AddArea(CreateView):
    model = Area
    form_class = AddAreaForm
    template_name = "users/edit/area_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Area added successfully')
        return super(AddArea, self).form_valid(form)

    def get_success_url(self):
        return reverse('edit_areas', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

    
class EducationListView(ListView):
    model = Education
    template_name = "users/edit/education_list.html"

    def get_queryset(self):
         return Education.objects.filter(user=self.request.user).order_by("-id")
         
    def get_context_data(self, **kwargs):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        context = super(EducationListView, self).get_context_data(**kwargs)
        return context
    
class UpdateEducation(UpdateView):
    model = Education
    template_name = "users/edit/education_form.html"
    form_class = EducationForm


    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Education.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Education Details")
                
        return Education.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.success(self.request,'Education #%d updated successfully ' % int(self.kwargs['pk']))
        return reverse('education_list', kwargs={'slug':self.request.user})
    
class AddEducation(CreateView):
    model = Education
    template_name = "users/edit/education_form.html"
    form_class = EducationForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        form.save()
        return super(AddEducation, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request,'New Education added successfully ')
        return reverse('education_list', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

class DelEducation(DeleteView):
    model = Education
    template_name = "users/edit/education_del.html"
    
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Education.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Education Details")
                
        return Education.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.warning(self.request,'Education #%d deleted successfully ' % int(self.kwargs['pk']))
        return reverse('education_list', kwargs={'slug':self.request.user})
        

class UserRoleListView(ListView):
    model = UserRole
    template_name = "users/edit/user_role_list.html"

    def get_queryset(self):
         return UserRole.objects.filter(user=self.request.user).order_by("-id")
         
    def get_context_data(self, **kwargs):
        if(self.request.user.rid != self.kwargs['slug']):
            raise PermissionDenied("Not allwoed to Edit others profile")
        context = super(UserRoleListView, self).get_context_data(**kwargs)
        return context

class AddUserRole(CreateView):
    model = UserRole
    form_class = UserRoleForm
    template_name = "users/edit/user_role_form.html"
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        form.save()
        messages.success(self.request,'New User Role added successfully')
        return super(AddUserRole, self).form_valid(form)

    def get_success_url(self):
        return reverse('user_role_list', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

    
class UpdateUserRole(UpdateView):
    model = UserRole
    template_name = "users/edit/user_role_form.html"
    form_class = UserRoleForm


    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != Education.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Role Details")
                
        return UserRole.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.success(self.request,'UserRole #%d updated successfully ' % int(self.kwargs['pk']))
        return reverse('user_role_list', kwargs={'slug':self.request.user})

class DelUserRole(DeleteView):
    model = UserRole
    template_name = "users/edit/user_role_del.html"
    
    def get_object(self, queryset=None):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
                
        if(self.request.user.rid != UserRole.objects.get(id=self.kwargs['pk']).user.rid):
		raise PermissionDenied("Not allwoed to Edit others Role Details")
                
        return UserRole.objects.filter(user=RidUser.objects.get(rid=self.request.user.rid)).get(id=self.kwargs['pk'])
    
    def get_success_url(self):
        messages.warning(self.request,'UserRole #%d deleted successfully ' % int(self.kwargs['pk']))
        return reverse('user_role_list', kwargs={'slug':self.request.user})

        
class AddRole(CreateView):
    model = Role
    form_class = AddRoleForm
    template_name = "users/edit/role_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Role added successfully')
        return super(AddRole, self).form_valid(form)

    def get_success_url(self):
        return reverse('user_role_add', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

class AddRolePermission(CreateView):
    model = RolePermission
    form_class = AddRolePermissionForm
    template_name = "users/edit/role_permission_add.html"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'New Role Permission added successfully')
        return super(AddRolePermission, self).form_valid(form)

    def get_success_url(self):
        return reverse('role_add', kwargs={'slug':self.request.user})

    def get_initial(self):
	if(self.request.user.rid != self.kwargs['slug']):
		raise PermissionDenied("Not allwoed to Edit others profile")
        pass

        
