from django import forms
from .models import Habit, DailyRecord

# class UserForm(forms.modelForm):
#     class Meta:
#         fields = ???

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('action', 'target', 'unit_of_measure')

class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ('habit',)
