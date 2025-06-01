from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/', views.create_post, name='create_post'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
]