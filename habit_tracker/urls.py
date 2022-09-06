from django.urls import path
from . import views

urlpatterns = [
    path('', views.Habit, name = 'Habit'),
]