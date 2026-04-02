from django import forms
from .models import Notice

class NoticeModelForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'body', 'photo']