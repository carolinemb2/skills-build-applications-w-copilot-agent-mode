from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'member_count', 'created_at']
    search_fields = ['name', 'description']
    filter_horizontal = ['members']

