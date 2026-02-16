from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class ModelTests(TestCase):
    """Test cases for Django models"""

    def setUp(self):
        """Set up test data"""
        self.team = Team.objects.create(
            name='Test Team',
            description='Test Description',
            total_points=100
        )
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team_id=self.team.id,
            total_points=50
        )

    def test_user_creation(self):
        """Test User model creation"""
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team_id, self.team.id)
        self.assertEqual(self.user.total_points, 50)

    def test_team_creation(self):
        """Test Team model creation"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'Test Description')
        self.assertEqual(self.team.total_points, 100)

    def test_activity_creation(self):
        """Test Activity model creation"""
        activity = Activity.objects.create(
            user_id=self.user.id,
            activity_type='Running',
            duration_minutes=30,
            points_earned=30,
            date=date.today()
        )
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration_minutes, 30)
        self.assertEqual(activity.points_earned, 30)

    def test_leaderboard_creation(self):
        """Test Leaderboard model creation"""
        leaderboard = Leaderboard.objects.create(
            user_id=self.user.id,
            user_name=self.user.name,
            team_name=self.team.name,
            total_points=self.user.total_points,
            rank=1
        )
        self.assertEqual(leaderboard.rank, 1)
        self.assertEqual(leaderboard.user_name, 'Test User')
        self.assertEqual(leaderboard.total_points, 50)

    def test_workout_creation(self):
        """Test Workout model creation"""
        workout = Workout.objects.create(
            name='Test Workout',
            description='Test workout description',
            difficulty_level='Medium',
            estimated_duration=45,
            points_value=45
        )
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty_level, 'Medium')
        self.assertEqual(workout.points_value, 45)


class APITests(APITestCase):
    """Test cases for REST API endpoints"""

    def setUp(self):
        """Set up test data"""
        self.team = Team.objects.create(
            name='API Test Team',
            description='API Test Description',
            total_points=200
        )
        self.user = User.objects.create(
            name='API Test User',
            email='apitest@example.com',
            team_id=self.team.id,
            total_points=100
        )

    def test_api_root(self):
        """Test API root endpoint"""
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_users_list(self):
        """Test GET /api/users/"""
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_users_retrieve(self):
        """Test GET /api/users/{id}/"""
        url = f'/api/users/{self.user.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test User')
        self.assertEqual(response.data['email'], 'apitest@example.com')

    def test_teams_list(self):
        """Test GET /api/teams/"""
        url = '/api/teams/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_retrieve(self):
        """Test GET /api/teams/{id}/"""
        url = f'/api/teams/{self.team.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Team')

    def test_activities_list(self):
        """Test GET /api/activities/"""
        Activity.objects.create(
            user_id=self.user.id,
            activity_type='Swimming',
            duration_minutes=60,
            points_earned=60,
            date=date.today()
        )
        url = '/api/activities/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_list(self):
        """Test GET /api/leaderboard/"""
        Leaderboard.objects.create(
            user_id=self.user.id,
            user_name=self.user.name,
            team_name=self.team.name,
            total_points=self.user.total_points,
            rank=1
        )
        url = '/api/leaderboard/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_list(self):
        """Test GET /api/workouts/"""
        Workout.objects.create(
            name='API Test Workout',
            description='Test description',
            difficulty_level='Easy',
            estimated_duration=30,
            points_value=30
        )
        url = '/api/workouts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_users_create(self):
        """Test POST /api/users/"""
        url = '/api/users/'
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'team_id': self.team.id,
            'total_points': 0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.filter(email='newuser@example.com').count(), 1)

    def test_teams_create(self):
        """Test POST /api/teams/"""
        url = '/api/teams/'
        data = {
            'name': 'New Team',
            'description': 'New team description',
            'total_points': 0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.filter(name='New Team').count(), 1)

    def test_users_update(self):
        """Test PUT /api/users/{id}/"""
        url = f'/api/users/{self.user.id}/'
        data = {
            'name': 'Updated User',
            'email': 'apitest@example.com',
            'team_id': self.team.id,
            'total_points': 150
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Updated User')
        self.assertEqual(self.user.total_points, 150)

    def test_users_delete(self):
        """Test DELETE /api/users/{id}/"""
        user = User.objects.create(
            name='Delete User',
            email='delete@example.com',
            team_id=self.team.id,
            total_points=0
        )
        url = f'/api/users/{user.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.filter(id=user.id).count(), 0)


class CORSTests(TestCase):
    """Test CORS configuration"""

    def test_cors_headers_present(self):
        """Test that CORS headers are configured"""
        from django.conf import settings
        self.assertTrue(settings.CORS_ALLOW_ALL_ORIGINS)
        self.assertIn('corsheaders', settings.INSTALLED_APPS)
        self.assertIn('corsheaders.middleware.CorsMiddleware', settings.MIDDLEWARE)
