from django.db import models
from django.contrib.auth.models import User

class LeaderboardEntry(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('all_time', 'All Time'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0, help_text="Total duration in minutes")
    total_distance = models.FloatField(default=0, help_text="Total distance in kilometers")
    total_calories = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    period_start = models.DateField()
    period_end = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['period', 'rank']
        unique_together = ['user', 'period', 'period_start']
    
    def __str__(self):
        return f"{self.user.username} - {self.period} - Rank {self.rank}"

