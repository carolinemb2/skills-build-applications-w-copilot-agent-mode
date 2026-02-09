from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel superheroes fitness team',
            total_points=0
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC superheroes fitness team',
            total_points=0
        )

        # Create Users (Superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            # Team Marvel
            {'name': 'Tony Stark', 'email': 'tony.stark@marvel.com', 'team': team_marvel, 'points': 1500},
            {'name': 'Steve Rogers', 'email': 'steve.rogers@marvel.com', 'team': team_marvel, 'points': 1800},
            {'name': 'Natasha Romanoff', 'email': 'natasha.romanoff@marvel.com', 'team': team_marvel, 'points': 1600},
            {'name': 'Bruce Banner', 'email': 'bruce.banner@marvel.com', 'team': team_marvel, 'points': 1200},
            {'name': 'Thor Odinson', 'email': 'thor.odinson@marvel.com', 'team': team_marvel, 'points': 2000},
            # Team DC
            {'name': 'Bruce Wayne', 'email': 'bruce.wayne@dc.com', 'team': team_dc, 'points': 1700},
            {'name': 'Clark Kent', 'email': 'clark.kent@dc.com', 'team': team_dc, 'points': 1900},
            {'name': 'Diana Prince', 'email': 'diana.prince@dc.com', 'team': team_dc, 'points': 1750},
            {'name': 'Barry Allen', 'email': 'barry.allen@dc.com', 'team': team_dc, 'points': 1650},
            {'name': 'Arthur Curry', 'email': 'arthur.curry@dc.com', 'team': team_dc, 'points': 1400},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                team_id=user_data['team'].id,
                total_points=user_data['points']
            )
            users.append(user)

        # Update team points
        team_marvel.total_points = sum([u['points'] for u in users_data if u['team'] == team_marvel])
        team_marvel.save()
        team_dc.total_points = sum([u['points'] for u in users_data if u['team'] == team_dc])
        team_dc.save()

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Swimming', 'Strength Training', 'Cycling', 'Yoga']
        today = date.today()
        
        for i, user in enumerate(users):
            for j in range(5):
                activity_date = today - timedelta(days=j)
                activity_type = activity_types[j % len(activity_types)]
                duration = 30 + (i * 5) + (j * 10)
                points = duration // 10
                
                Activity.objects.create(
                    user_id=user.id,
                    activity_type=activity_type,
                    duration_minutes=duration,
                    points_earned=points,
                    date=activity_date
                )

        # Create Leaderboard
        self.stdout.write('Creating leaderboard...')
        sorted_users = sorted(users, key=lambda u: u.total_points, reverse=True)
        
        for rank, user in enumerate(sorted_users, start=1):
            team = Team.objects.get(id=user.team_id)
            Leaderboard.objects.create(
                user_id=user.id,
                user_name=user.name,
                team_name=team.name,
                total_points=user.total_points,
                rank=rank
            )

        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'Intense full-body workout designed for peak performance',
                'difficulty_level': 'Hard',
                'estimated_duration': 60,
                'points_value': 60
            },
            {
                'name': 'Web Slinger Cardio',
                'description': 'High-intensity cardio workout to build endurance',
                'difficulty_level': 'Medium',
                'estimated_duration': 45,
                'points_value': 45
            },
            {
                'name': 'Stark Industries Core',
                'description': 'Core strengthening exercises for stability',
                'difficulty_level': 'Medium',
                'estimated_duration': 30,
                'points_value': 30
            },
            {
                'name': 'Amazon Warrior Strength',
                'description': 'Strength training for maximum power',
                'difficulty_level': 'Hard',
                'estimated_duration': 50,
                'points_value': 50
            },
            {
                'name': 'Flash Speed Training',
                'description': 'Sprint intervals and agility drills',
                'difficulty_level': 'Medium',
                'estimated_duration': 40,
                'points_value': 40
            },
            {
                'name': 'Aquaman Swimming',
                'description': 'Swimming workout for full-body conditioning',
                'difficulty_level': 'Easy',
                'estimated_duration': 35,
                'points_value': 35
            },
            {
                'name': 'Hulk Smash Workout',
                'description': 'High-intensity interval training',
                'difficulty_level': 'Hard',
                'estimated_duration': 55,
                'points_value': 55
            },
            {
                'name': 'Black Widow Flexibility',
                'description': 'Yoga and stretching for flexibility',
                'difficulty_level': 'Easy',
                'estimated_duration': 30,
                'points_value': 30
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data!'))
        self.stdout.write(f'Created {Team.objects.count()} teams')
        self.stdout.write(f'Created {User.objects.count()} users')
        self.stdout.write(f'Created {Activity.objects.count()} activities')
        self.stdout.write(f'Created {Leaderboard.objects.count()} leaderboard entries')
        self.stdout.write(f'Created {Workout.objects.count()} workouts')
