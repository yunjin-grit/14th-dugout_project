from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#DjangoProject\blogProject\blog\models.py

class Team(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self): 
        return self.title


class Diary(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    image = models.ImageField(upload_to='diary/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    image = models.ImageField(upload_to='diary/', blank=True, null=True)

    def __str__(self): 
        return self.title