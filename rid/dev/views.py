from django.shortcuts import render
from django.contrib.auth.decorators import login_required as auth

@auth
def DevIntro(request):
        return render(request, "dev/intro.html")

