from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'team_id', 'total_points', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'total_points', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'activity_type', 'duration_minutes', 'points_earned', 'date')
    search_fields = ('activity_type',)
    list_filter = ('activity_type', 'date')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_name', 'team_name', 'total_points', 'updated_at')
    search_fields = ('user_name', 'team_name')
    list_filter = ('updated_at',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'difficulty_level', 'estimated_duration', 'points_value', 'created_at')
    search_fields = ('name', 'difficulty_level')
    list_filter = ('difficulty_level', 'created_at')
