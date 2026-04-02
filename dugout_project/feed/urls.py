from django.contrib import admin
from django.urls import path
from feed import views

urlpatterns = [
    path("", views.feed, name="feed"), 
    path('create/', views.create, name='feed_create'),
    path("feed_list/", views.feed_list, name="feed_list"), 
    path("feed_detail/<int:feed_id>/", views.feed_detail, name="feed_detail"),
    path("feed_update/<int:id>/", views.feed_update, name="feed_update"),
    path("feed_delete/<int:id>/", views.feed_delete, name="feed_delete"),

    path('create_comment/<int:id>/', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>/', views.delete_comment, name='delete_comment'),
]