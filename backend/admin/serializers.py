from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from .utils import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('name', 'assignee', 'finished', 'finishedTime', 'assignee_avatars')
    # total = serializers.SerializerMethodField('get_total')
    assignee = serializers.SerializerMethodField('fix_assignee')
    assignee_avatars = serializers.SerializerMethodField('get_assignee_avatars')
    name = serializers.SerializerMethodField('fix_name')
    def fix_name(self, obj):
        if len(obj.name) > 80:
            return obj.name[0:80]+u'...'
        return obj.name
    def fix_assignee(self, obj):
        return ','.join(obj.assignee.split(',')[0:3])
    def get_total(self, obj):
        return Task.objects.count()
    def get_assignee_avatars(self, obj):
        return ",".join([getPersonImg(i.strip()) for i in obj.assignee.split(',')[0:3]])

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'progress')

