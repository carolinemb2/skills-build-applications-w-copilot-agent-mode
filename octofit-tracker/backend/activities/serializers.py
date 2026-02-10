from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User

class ActivitySerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_username', 'activity_type', 'duration', 'distance', 
                  'calories', 'notes', 'activity_date', 'created_at']
        read_only_fields = ['id', 'created_at']
