from django import forms
from .models import Notices

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notices
        exclude = ("sender",)
        
        widgets = {
            'receiver' : forms.Select(attrs={'class':'fluid four wide'}),
            'title' : forms.TextInput(attrs={'placeholder':'Enter your Title'}),
            'body': forms.Textarea(attrs={'placeholder':'Enter your body','rows':'30', 'cols':'40'}),
            'attachment' : forms.FileInput(attrs={'id':'attachmentName','style':'display:none'}),
        } 
