from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
        user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')

        # Create teams
        team = Team.objects.create(name='FitSquad')
        team.members.add(user1, user2)

        # Create activities
        Activity.objects.create(user=user1, activity_type='Running', duration=45, calories=350, date=datetime(2026,2,9,8,0))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=60, calories=500, date=datetime(2026,2,9,9,0))

        # Create leaderboard
        Leaderboard.objects.create(user=user1, points=1200, rank=1)
        Leaderboard.objects.create(user=user2, points=1100, rank=2)

        # Create workouts
        Workout.objects.create(user=user1, workout_type='Yoga', suggested=True, date=datetime(2026,2,9,10,0))
        Workout.objects.create(user=user2, workout_type='HIIT', suggested=False, date=datetime(2026,2,9,11,0))

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
