"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from habit_tracker import views

urlpatterns = [
    path('', views.home, name='home'),
    # You need this for django-registration-redux
    path("auth/", include("registration.backends.simple.urls")),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('habit_tracker/<int:pk>', views.Habit, name = 'habit_record'),
    path('habit_tracker/new', views.create_habit, name='create_habit'),
    path('habit_tracker/<int:pk>/edit', views.edit_habit, name='edit_habit'),
    path('habit_tracker/<int:pk>/delete', views.delete_habit, name='delete'),
]
