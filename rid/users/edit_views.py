from django.shortcuts import render

def EditProfilePicView(request):
    return render(request, "users/edit/profile_pic.html")
