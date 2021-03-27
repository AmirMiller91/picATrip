from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewPosts, name='picogram-viewPosts'),
    path('addPost', views.addPost, name='picogram-addPost'),
]
