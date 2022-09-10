from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.decorators import login_required

class User(AbstractUser):
    def __str__(self):
        return self.username


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'habits')
    created_at = models.DateField(db_index=True, auto_now_add=True, null=True)
    action = models.CharField(max_length=250)
    target = models.IntegerField()
    unit_of_measure = models.CharField(max_length=250)

    def __str__(self):
        return self.action


class DailyRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name= 'habits')
    date = models.DateField(null=True)
    target_completed = models.IntegerField(null=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_constraint')
        ]

    def __str__(self):
        return str(self.date)
