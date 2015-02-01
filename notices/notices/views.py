from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Notices
from .forms import NoticeForm
from django.contrib import messages


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
    #messages.warning(self.request, "Notice Deleted Successfully")
    success_url = reverse_lazy("notices")

class UpdateNotice(UpdateView):
    model = Notices
    form_class = NoticeForm
    success_url = reverse_lazy("notices")
