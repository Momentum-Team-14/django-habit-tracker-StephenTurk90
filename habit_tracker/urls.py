from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # You need this for django-registration-redux
    path("auth/", include("registration.backends.simple.urls")),
    path("admin/", admin.site.urls),
]
