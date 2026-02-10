from django.db import models
from django.contrib.auth.models import User

class WorkoutSuggestion(models.Model):
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    CATEGORY_CHOICES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
        ('mixed', 'Mixed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_estimate = models.IntegerField(help_text="Estimated calories burned")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.difficulty})"

class UserWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_workouts')
    workout = models.ForeignKey(WorkoutSuggestion, on_delete=models.CASCADE, related_name='user_workouts')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, help_text="Rating from 1-5")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.workout.title}"

