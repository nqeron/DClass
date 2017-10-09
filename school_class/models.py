from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy
from multiselectfield import MultiSelectField

CHECKBOX_CHOICES = (('M','Monday'),('T','Tuesday'),('W','Wednesday'),('Th','Thursday'),('F','Friday'))
User = get_user_model()
# from students.models import Student
# Create your models here.

class SchoolClass(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    teacher = models.CharField(max_length=256)
    location = models.CharField(blank=True, max_length=100)
    days_of_week = MultiSelectField(blank=True, max_length=100, choices=CHECKBOX_CHOICES)
    start_time = models.TimeField(blank=False,default="12:00")
    end_time = models.TimeField(blank=False,default="12:00")

    def __str__(self):
        return self.name

    def clean(self):
        # Make sure that end_time is after start_time
        if self.start_time >= self.end_time:
            raise ValidationError(ugettext_lazy('Start time must be before end time!'))

    def getTimes(self):
        return self.days_of_week,self.start_time,self.end_time
    #     ('M,W,Th',2:15,3:15)
