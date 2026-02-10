from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WorkoutSuggestion, UserWorkout
from .serializers import WorkoutSuggestionSerializer, UserWorkoutSerializer

class WorkoutSuggestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        difficulty = request.query_params.get('difficulty', 'beginner')
        workouts = WorkoutSuggestion.objects.filter(difficulty=difficulty)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category', 'cardio')
        workouts = WorkoutSuggestion.objects.filter(category=category)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)

class UserWorkoutViewSet(viewsets.ModelViewSet):
    queryset = UserWorkout.objects.all()
    serializer_class = UserWorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return UserWorkout.objects.all()
        return UserWorkout.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def my_workouts(self, request):
        workouts = UserWorkout.objects.filter(user=request.user)
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)

