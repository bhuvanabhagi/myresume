# App_08_3/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.resume_view, name='resume'),
    path('resume/photo.jpg', views.photo_view, name='photo'), 
]
