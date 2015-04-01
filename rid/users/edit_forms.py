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

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
	fields = ['url','email','mobile']
        widgets = {
           'url' : forms.URLInput(attrs={'placeholder':'Enter your website / blog url'}),
           'email' : forms.EmailInput(attrs={'placeholder':'Enter your email address '}),
           'mobile' : forms.TextInput(attrs={'placeholder':'Enter your mobile number', 'style':'max-length:11'}),
        }
