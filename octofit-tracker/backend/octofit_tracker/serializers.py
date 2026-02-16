from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj._id)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj._id)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_id(self, obj):
        return str(obj.user._id)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'calories', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_id(self, obj):
        return str(obj.user._id)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'points', 'rank']

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_id(self, obj):
        return str(obj.user._id)
    
    class Meta:
        model = Workout
        fields = ['id', 'user_id', 'workout_type', 'suggested', 'date']
