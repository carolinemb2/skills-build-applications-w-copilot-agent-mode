from rest_framework import serializers
from .models import LeaderboardEntry

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_username', 'period', 'total_activities', 
                  'total_duration', 'total_distance', 'total_calories', 'rank',
                  'period_start', 'period_end', 'updated_at']
        read_only_fields = ['id', 'updated_at']
