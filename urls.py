# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upcoming-ipos/', views.upcoming_ipos, name='upcoming_ipos'),
]
