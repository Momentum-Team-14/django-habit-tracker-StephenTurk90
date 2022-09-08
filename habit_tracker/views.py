from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from django.shortcuts import redirect


def home(request):
    return render(request, "habit/home.html")

