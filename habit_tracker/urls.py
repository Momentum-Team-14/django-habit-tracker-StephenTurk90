from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # You need this for django-registration-redux
    path("auth/", include("registration.backends.simple.urls")),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('habit_tracker/<int:pk>', views.habit_record, name = 'habit_record'),
    path('habit_tracker/new', views.create_habit, name='create_habit'),
    path('habit_tracker/<int:pk>/edit', views.edit_habit, name='edit_habit'),
    path('habit_tracker/<int:pk>/delete', views.delete_habit, name='delete'),
]