from django.views.generic import ListView
from django.shortcuts import render
from .models import Notices

def HomePageView(request):
    return render(request, "home.html")

class NoticesView(ListView):
    model = Notices
    paginate_by = 5



