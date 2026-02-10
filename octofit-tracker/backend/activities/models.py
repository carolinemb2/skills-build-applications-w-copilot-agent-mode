from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('walking', 'Walking'),
        ('gym', 'Gym Workout'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    distance = models.FloatField(null=True, blank=True, help_text="Distance in kilometers")
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    activity_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-activity_date']
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.activity_date.date()}"

