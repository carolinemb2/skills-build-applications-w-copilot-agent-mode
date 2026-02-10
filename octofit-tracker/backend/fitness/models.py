from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """Extended user profile for fitness tracking"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    fitness_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], default='beginner')
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Team(models.Model):
    """Team model for group competitions"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_points(self):
        """Calculate total points for all team members"""
        return sum(member.profile.total_points for member in self.members.all() if hasattr(member, 'profile'))


class Activity(models.Model):
    """Activity log for fitness tracking"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('strength', 'Strength Training'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration_minutes = models.IntegerField(help_text='Duration in minutes')
    distance = models.FloatField(null=True, blank=True, help_text='Distance in miles')
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    points = models.IntegerField(default=0)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"

    def save(self, *args, **kwargs):
        """Calculate points based on activity"""
        if not self.points:
            # Simple point calculation: 1 point per minute
            self.points = self.duration_minutes
        super().save(*args, **kwargs)
        
        # Update user's total points
        if hasattr(self.user, 'profile'):
            total = sum(activity.points for activity in self.user.activities.all())
            self.user.profile.total_points = total
            self.user.profile.save()


class WorkoutSuggestion(models.Model):
    """Personalized workout suggestions"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    fitness_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    activity_type = models.CharField(max_length=20, choices=Activity.ACTIVITY_TYPES)
    duration_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.fitness_level})"

