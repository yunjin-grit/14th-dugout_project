from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path("info/", views.info, name="info"), 
    path('', views.home, name='home'),
    path('create/', views.diary_create, name='diary_create'), 
    path("diary_list/", views.diary_list, name="diary_list"), 
    path('diary/<int:id>/', views.diary_detail, name='diary_detail'),
    path('update/<int:id>/', views.diary_update, name='diary_update'),
    path('delete/<int:id>/', views.diary_delete, name='diary_delete'),
]