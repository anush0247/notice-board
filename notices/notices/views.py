from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Notices
from .forms import AddNoticeForm
from django.contrib import messages

def HomePageView(request):
    return render(request, "home.html")
    
class NoticesView(ListView):
    model = Notices
    paginate_by = 10

class OneNoticeView(DetailView):
    model = Notices

class AddNotice(CreateView):
    model = Notices
    form_class = AddNoticeForm
    success_url = reverse_lazy("notice_add")
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.sender = self.request.user
        f.save()
        messages.success(self.request,'New Notice added successfully')
        return super(AddNotice, self).form_valid(form)

