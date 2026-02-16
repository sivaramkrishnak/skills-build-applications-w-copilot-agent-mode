from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')

        # Create users
        User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team_name='Marvel')
        User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team_name='Marvel')
        User.objects.create_user(username='batman', email='batman@dc.com', password='password', team_name='DC')
        User.objects.create_user(username='superman', email='superman@dc.com', password='password', team_name='DC')

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30)
        Activity.objects.create(user_email='batman@dc.com', type='cycle', duration=45)
        Activity.objects.create(user_email='superman@dc.com', type='swim', duration=60)
        Activity.objects.create(user_email='captain@marvel.com', type='walk', duration=20)

        # Create workouts
        Workout.objects.create(user_email='ironman@marvel.com', description='Chest workout')
        Workout.objects.create(user_email='batman@dc.com', description='Leg workout')
        Workout.objects.create(user_email='superman@dc.com', description='Cardio workout')
        Workout.objects.create(user_email='captain@marvel.com', description='Arm workout')

        # Create leaderboard
        Leaderboard.objects.create(team_name='Marvel', points=100)
        Leaderboard.objects.create(team_name='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
