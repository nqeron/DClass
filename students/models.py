from django.db import models
from django.contrib import auth
from school_class.models import SchoolClass
# Create your models here.

class Student(auth.models.User,auth.models.PermissionsMixin):
    classes = models.ManyToManyField(SchoolClass)

    def __str__(self):
        return self.username

    def getClassTimes(self):
        times = {}
        for c in self.classes.all():
            days,start_time,end_time=c.getTimes()
            for d in days:
                if not (d in times):
                    times[d] = [(start_time,end_time,c)]
                else:
                    times[d] += [(start_time,end_time,c)]
        return times

    # def getClassSchedule(self):
    #     sched = { '0700' : {'Monday' : []}}
