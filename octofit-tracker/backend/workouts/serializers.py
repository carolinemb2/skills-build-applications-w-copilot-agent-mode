from rest_framework import serializers
from .models import WorkoutSuggestion, UserWorkout

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'title', 'description', 'category', 'difficulty', 
                  'duration', 'calories_estimate', 'created_at']
        read_only_fields = ['id', 'created_at']

class UserWorkoutSerializer(serializers.ModelSerializer):
    workout_title = serializers.CharField(source='workout.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = UserWorkout
        fields = ['id', 'user', 'user_username', 'workout', 'workout_title', 
                  'completed', 'completed_at', 'rating', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']
