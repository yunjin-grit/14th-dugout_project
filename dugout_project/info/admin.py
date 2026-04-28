from django.contrib import admin
from .models import Diary 

admin.site.register(Diary)

# Register your models here.
from .models import Team 

admin.site.register(Team)