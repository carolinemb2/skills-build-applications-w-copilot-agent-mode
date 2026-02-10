from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Team, Activity, WorkoutSuggestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'username', 'bio', 'fitness_level', 'total_points', 'created_at', 'updated_at']


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    total_points = serializers.ReadOnlyField()
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'member_count', 'created_by', 'total_points', 'created_at', 'updated_at']

    def get_member_count(self, obj):
        return obj.members.count()


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'username', 'activity_type', 'duration_minutes', 'distance', 'calories', 
                  'notes', 'points', 'date', 'created_at', 'updated_at']
        read_only_fields = ['points']


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'title', 'description', 'fitness_level', 'activity_type', 'duration_minutes', 'created_at']
