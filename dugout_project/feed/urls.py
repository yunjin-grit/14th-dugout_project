from django.contrib import admin
from django.urls import path
from feed import views

urlpatterns = [
    path("", views.feed, name="feed"), 
    path("feed_list/", views.feed_list, name="feed_list"), 
    path("feed_detail/<int:feed_id>/", views.feed_detail, name="feed_detail"),
    path("feed_update/<int:id>/", views.feed_update, name="feed_update"),
    path("feed_delete/<int:id>/", views.feed_delete, name="feed_delete"),
]