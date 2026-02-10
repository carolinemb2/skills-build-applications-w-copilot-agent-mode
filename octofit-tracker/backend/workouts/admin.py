from django.contrib import admin
from .models import WorkoutSuggestion, UserWorkout

@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'duration', 'calories_estimate']
    list_filter = ['category', 'difficulty']
    search_fields = ['title', 'description']

@admin.register(UserWorkout)
class UserWorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'workout', 'completed', 'completed_at', 'rating']
    list_filter = ['completed', 'rating']
    search_fields = ['user__username', 'workout__title']

