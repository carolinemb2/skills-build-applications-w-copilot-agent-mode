from django.contrib import admin
from .models import LeaderboardEntry

@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'period', 'rank', 'total_activities', 'total_duration', 'period_start']
    list_filter = ['period', 'period_start']
    search_fields = ['user__username']

