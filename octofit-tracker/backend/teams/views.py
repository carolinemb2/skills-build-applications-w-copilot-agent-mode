from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        team = serializer.save(created_by=self.request.user)
        team.members.add(self.request.user)
    
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        team = self.get_object()
        team.members.add(request.user)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def leave(self, request, pk=None):
        team = self.get_object()
        team.members.remove(request.user)
        serializer = self.get_serializer(team)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def my_teams(self, request):
        teams = Team.objects.filter(members=request.user)
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)

