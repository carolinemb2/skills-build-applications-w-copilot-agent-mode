from rest_framework import serializers
from .models import Team
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    member_count = serializers.IntegerField(read_only=True)
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_by', 'created_by_username', 
                  'members', 'member_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
