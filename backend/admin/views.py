from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.finishedTask.all()
        serializer = TaskSerializer(tasks, many=True)
        json = {}
        json['data'] = serializer.data
        json['total'] = Task.object.count()
        return Response(json)

class TaskViewSet(viewsets.ModelViewSet):
    """docstring for TaskViewSet"""
    queryset = Task.finishedTask.all()
    serializer_class = TaskSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """docstring for TaskViewSet"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer