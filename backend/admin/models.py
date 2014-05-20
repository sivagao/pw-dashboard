#-*-coding:utf-8-*-

from django.db import models

class FinishedTaskManager(models.Manager):
    def get_queryset(self):
        return super(FinishedTaskManager, self).get_queryset().filter(finished=True)

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, help_text=u'Polish Weeek 任务名称', verbose_name=u'任务名称')
    assignee = models.CharField(max_length=255, help_text=u',英文逗号分割的人名', verbose_name=u'完成者')
    finished = models.BooleanField(default=False, help_text=u'完成与否', verbose_name=u'完全情况')

    created = models.DateTimeField(auto_now_add=True)
    finishedTime = models.DateTimeField(auto_now=True)


    object = models.Manager()
    # objects = FinishedTaskManager()
    # allTask = models.Manager() # The default manager.
    finishedTask = FinishedTaskManager()

    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255, help_text=u'Polish Weeek 小组名称', verbose_name=u'小组名称')
    progress = models.DecimalField(max_digits=5, decimal_places=2, help_text=u'完成到第几步啦', verbose_name=u'进度')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, is %d' % (self.name, self.progress)