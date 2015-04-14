from django.shortcuts import render
from django.contrib.auth.decorators import login_required as auth

@auth
def DevDoc(request):
        return render(request, "dev/docs.html")

