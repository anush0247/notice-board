from django import forms
from users.models import Profile

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        #exclude = ("mobile","url","email","summary","skills","areas",)
	fields = ['profile_pic']
        widgets = {
           'profile_pic' : forms.FileInput(attrs={'id':'attachmentName','style' : 'display:none;',}),
        }
