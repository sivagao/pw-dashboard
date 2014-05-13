from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignee', 'finished', 'finishedTime', 'admin_assignee_avatars')

    """ List extensions """
    def admin_assignee_avatars(self, obj):
        return "".join([ '<img src="http://who.wandoulabs.com/static/img/%s.jpg" style="width: 80px;margin: 0 5px;">' % i.strip() for i in obj.assignee.split(',') ])

    admin_assignee_avatars.allow_tags = True

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress','modified')

admin.site.register(Task, TaskAdmin)
admin.site.register(Team, TeamAdmin)
