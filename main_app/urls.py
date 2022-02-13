from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('profiles/create/', views.profile_create, name='profiles_create'),
]
