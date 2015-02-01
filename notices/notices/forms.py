from django import forms
from .models import Notices

class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notices
        exclude = ("sender",)
        widgets = {
            'receiver' : forms.Select(attrs={'class':'fluid four wide'}),
        } 
