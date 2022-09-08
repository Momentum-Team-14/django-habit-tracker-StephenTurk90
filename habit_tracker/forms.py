from django import forms
from .models import Habit, DailyRecord


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('action', 'date', 'target', 'unit_of_measure')

class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ('date',)
