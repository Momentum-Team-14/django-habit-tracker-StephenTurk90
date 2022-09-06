from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit
from .forms import HabitForm
from django.shortcuts import redirect

class HabitForm:
    class Meta:
        model = Habit
        fields = ('title',)