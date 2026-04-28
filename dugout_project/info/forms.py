from django import forms
from .models import Team
from .models import Diary

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'body']  

class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'image', 'body'] 