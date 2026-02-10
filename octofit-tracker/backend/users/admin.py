from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fitness_goal', 'created_at']
    search_fields = ['user__username', 'fitness_goal']

