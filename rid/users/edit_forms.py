from django import forms
from users.models import Profile,Skill
from django.forms.widgets import CheckboxSelectMultiple  

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

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Profile
	fields = ['skills',]
        #widgets = 
        #   'skills' : forms.URLInput(attrs={'placeholder':'Enter your website / blog url'}),
        #}

    def __init__(self, *args, **kwargs):

        super(SkillsForm, self).__init__(*args, **kwargs)

        self.fields["skills"].widget = CheckboxSelectMultiple()
        self.fields["skills"].queryset = Skill.objects.all() 
