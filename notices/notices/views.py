from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Notices, Profile
from .forms import NoticeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from oauth2_provider.views.generic import ProtectedResourceView


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')
        
def HomePageView(request):
    return render(request, "home.html")
    
class NoticesView(ListView):
    model = Notices
    paginate_by = 5
    
    def get_queryset(self):
        if(self.args) :
            return Notices.objects.filter(receiver=self.args[0]).order_by("-id")
        else:
            return Notices.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(NoticesView, self).get_context_data(**kwargs)
        if(self.args):
            context['year'] = self.args[0]
        else :
            context['year'] = "All"
        return context

class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_profile.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        Profile.objects.get_or_create(user=user)
        return user
        
class OneNoticeView(DetailView):
    model = Notices

    
class AddNotice(CreateView):
    model = Notices
    form_class = NoticeForm
    success_url = reverse_lazy("notice_add")
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.sender = self.request.user
        f.save()
        messages.success(self.request,'New Notice added successfully')
        return super(AddNotice, self).form_valid(form)
        
class DelNotice(DeleteView):
    model = Notices
    
    def get_success_url(self):
        messages.warning(self.request,'Notice #'+str(self.object.pk)+' deleted successfully')
        return reverse('notices')

class UpdateNotice(UpdateView):
    model = Notices
    form_class = NoticeForm

    def get_success_url(self):
        messages.success(self.request,'Notice #'+str(self.object.pk)+' updated successfully')
        return reverse('notice_detail', kwargs={'pk':self.object.pk})
