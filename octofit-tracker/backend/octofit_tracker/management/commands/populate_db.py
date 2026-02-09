from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):        
        # Create users
        self.stdout.write('Creating users...')
        user1 = User.objects.create(username='alice', email='alice@example.com', first_name='Alice', last_name='Smith')
        user2 = User.objects.create(username='bob', email='bob@example.com', first_name='Bob', last_name='Jones')
        user3 = User.objects.create(username='charlie', email='charlie@example.com', first_name='Charlie', last_name='Brown')
        
        self.stdout.write(f'Created user: {user1.username}')
        self.stdout.write(f'Created user: {user2.username}')
        self.stdout.write(f'Created user: {user3.username}')

        # Create teams
        self.stdout.write('Creating teams...')
        team1 = Team.objects.create(name='FitSquad')
        team2 = Team.objects.create(name='PowerLifters')
        self.stdout.write(f'Created team: {team1.name}')
        self.stdout.write(f'Created team: {team2.name}')

        # Create activities - use user object directly
        self.stdout.write('Creating activities...')
        Activity.objects.create(user=user1, activity_type='Running', duration=45, calories=350, date=datetime(2026,2,9,8,0))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=60, calories=500, date=datetime(2026,2,9,9,0))
        Activity.objects.create(user=user3, activity_type='Swimming', duration=30, calories=250, date=datetime(2026,2,9,10,0))
        Activity.objects.create(user=user1, activity_type='Yoga', duration=60, calories=200, date=datetime(2026,2,8,7,0))
        self.stdout.write('Created 4 activities')

        # Create leaderboard
        self.stdout.write('Creating leaderboard entries...')
        Leaderboard.objects.create(user=user1, points=1200, rank=1)
        Leaderboard.objects.create(user=user2, points=1100, rank=2)
        Leaderboard.objects.create(user=user3, points=950, rank=3)
        self.stdout.write('Created 3 leaderboard entries')

        # Create workouts
        self.stdout.write('Creating workouts...')
        Workout.objects.create(user=user1, workout_type='Yoga', suggested=True, date=datetime(2026,2,10,10,0))
        Workout.objects.create(user=user2, workout_type='HIIT', suggested=False, date=datetime(2026,2,10,11,0))
        Workout.objects.create(user=user3, workout_type='Strength Training', suggested=True, date=datetime(2026,2,10,14,0))
        self.stdout.write('Created 3 workouts')

        self.stdout.write(self.style.SUCCESS('\n✓ Test data populated successfully!'))
