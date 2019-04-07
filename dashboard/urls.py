from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Dash-home"),
    path('profile/', views.profile, name="profileAdd"),
]