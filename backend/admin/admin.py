#-*-coding:utf-8-*-

from django.contrib import admin
from .models import *
from .utils import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignee', 'finished', 'finishedTime', 'admin_assignee_avatars')

    """ List extensions """
    def admin_assignee_avatars(self, obj):
        return "".join([ '<img src="%s" style="width: 60px;margin: 0 5px;">' % getPersonImg(i.strip()) for i in obj.assignee.split(',') ])
        # cant use this, biz we dont know if the img/<name>.jpg is exist, which can be testing by requests cost tootoo much
        # return "".join([ '<img src="http://who.wandoulabs.com/static/img/%s.jpg" style="width: 80px;margin: 0 5px;">' % i.strip() for i in obj.assignee.split(',') ])

    admin_assignee_avatars.allow_tags = True
    admin_assignee_avatars.short_description = u'从who.wandoulabs去头像'

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress','modified')

admin.site.register(Task, TaskAdmin)
admin.site.register(Team, TeamAdmin)
