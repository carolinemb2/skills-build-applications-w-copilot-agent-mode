from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def daily(self, request):
        entries = LeaderboardEntry.objects.filter(period='daily').order_by('rank')
        serializer = self.get_serializer(entries, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def weekly(self, request):
        entries = LeaderboardEntry.objects.filter(period='weekly').order_by('rank')
        serializer = self.get_serializer(entries, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def monthly(self, request):
        entries = LeaderboardEntry.objects.filter(period='monthly').order_by('rank')
        serializer = self.get_serializer(entries, many=True)
        return Response(serializer.data)

