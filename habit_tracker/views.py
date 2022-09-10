from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from django.shortcuts import redirect


def home(request):
    habit = Habit.objects.all()
    return render(request, "habit/home.html", {'habit': habit})


def habit_record(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habit/habit_record.html', {'habit': habit})


def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect('habit_record', pk=habit.pk)
    else:
        form = HabitForm()
    return render(request, 'habit/create_habit.html', {'form': form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
            return redirect('habit_record', pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    return render(request, 'habit/edit_habit.html', {'form': form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('home')
