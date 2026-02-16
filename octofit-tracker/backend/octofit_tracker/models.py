from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, null=True)

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    user_email = models.EmailField()
    description = models.CharField(max_length=200)

class Leaderboard(models.Model):
    team_name = models.CharField(max_length=100)
    points = models.IntegerField()
