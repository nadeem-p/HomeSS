from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signIn, name='Sign In'),
    path('postsignIn/', views.postsignIn),
    path('postsignup/', views.postsignup),
    path('logout/', views.logout, name="logout"),
]