from django import forms
from .models import Team

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'body']  