from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class DailyRecord(models.Model):
    date = models.DateField()

    def __str__(self):
        return self.date


class Habit(models.Model):
    action = models.CharField(max_length=250)
    date = models.ForeignKey(DailyRecord, on_delete=models.CASCADE)
    target = models.IntegerField()
    unit_of_measure = models.CharField(max_length=250)

    def __str__(self):
        return self.habit
