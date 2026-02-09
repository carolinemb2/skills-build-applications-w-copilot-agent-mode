from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team_id = models.IntegerField(null=True, blank=True)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Team(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teams'


class Activity(models.Model):
    user_id = models.IntegerField()
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    points_earned = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.duration_minutes} mins"

    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'activities'


class Leaderboard(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200, blank=True)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rank}. {self.user_name} - {self.total_points} points"

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50)
    estimated_duration = models.IntegerField()
    points_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workouts'
