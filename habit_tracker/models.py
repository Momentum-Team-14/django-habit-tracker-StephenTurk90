from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Habit(models.Model):
    title = models.CharField(max_length=250)


    def __str__(self):
        return self.title