from django.contrib.auth import get_user_model
from django.views.generic import DetailView, ListView
from django.shortcuts import render

from auth.models import Profile, Education, Experience, Achievements

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
        context['education']   = Education.objects.filter(user=RUser.objects.filter(rid=str(self.kwargs['slug'])))
        context['experience']   = Experience.objects.filter(user=RUser.objects.filter(rid=str(self.kwargs['slug'])))
        context['achievements']   = Achievements.objects.filter(user=RUser.objects.filter(rid=str(self.kwargs['slug'])))        
        
        return context
        #pass
        
from auth.models import RUser

def DeptView(request):
    return render(request, "users/depts.html")

class DeptDetailView(ListView):
    models = RUser
    paginate_by = 4
    
    def get_queryset(self):
        if(len(self.args) == 2 ):
            return RUser.objects.filter(dept=self.args[0]).filter(batch=self.args[1])
        else :
            return RUser.objects.filter(dept=self.args[0])
            
    def get_context_data(self, **kwargs):       
        dept_dict = dict(RUser.department_labels)
        if self.args[0] in dept_dict :
            context = super(DeptDetailView, self).get_context_data(**kwargs)
            context['dept_full_name'] = dept_dict[self.args[0]]
            context['dept_code'] = self.args[0]
            tmp = ()
            for b in RUser.batch_labels:
                tmp += ( (b+(RUser.objects.filter(dept=self.args[0]).filter(batch=b[0]).count(),),) , )
                context['batch_tuple'] = tmp
            if ( len(self.args) == 2):
                batch_dict = dict(RUser.batch_labels)
                if self.args[1] in batch_dict :
                    context['batch_code'] = self.args[1]
                    context['batch_full_name'] = batch_dict[self.args[1]]
                else :
                    raise ValueError('Batch \'%s\' Not found' % (self.args[1]))
            else :
                context['batch_full_name'] = "All Users"
                
            return context
        else :
            raise ValueError('Department \'%s\' Not found' %(self.args[0]))
        
