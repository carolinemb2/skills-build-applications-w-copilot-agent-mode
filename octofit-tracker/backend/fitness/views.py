from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import UserProfile, Team, Activity, WorkoutSuggestion
from .serializers import (
    UserProfileSerializer, TeamSerializer, ActivitySerializer, 
    WorkoutSuggestionSerializer, UserSerializer
)


@api_view(['GET'])
def api_root(request):
    """API root endpoint"""
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'users': '/api/users/',
            'profiles': '/api/profiles/',
            'teams': '/api/teams/',
            'activities': '/api/activities/',
            'leaderboard': '/api/leaderboard/',
            'workout-suggestions': '/api/workout-suggestions/',
        }
    })


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for user profiles"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by user if specified
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for teams"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        # Add creator as a member
        team.members.add(self.request.user)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        """Join a team"""
        team = self.get_object()
        team.members.add(request.user)
        return Response({'status': 'joined team'})

    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        """Leave a team"""
        team = self.get_object()
        team.members.remove(request.user)
        return Response({'status': 'left team'})


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for activities"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by user if specified
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        # Filter by activity type if specified
        activity_type = self.request.query_params.get('type', None)
        if activity_type:
            queryset = queryset.filter(activity_type=activity_type)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutSuggestionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for workout suggestions (read-only)"""
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by fitness level if specified
        fitness_level = self.request.query_params.get('level', None)
        if fitness_level:
            queryset = queryset.filter(fitness_level=fitness_level)
        return queryset


@api_view(['GET'])
def leaderboard(request):
    """Leaderboard endpoint showing top users by points"""
    limit = int(request.query_params.get('limit', 10))
    profiles = UserProfile.objects.order_by('-total_points')[:limit]
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data)

