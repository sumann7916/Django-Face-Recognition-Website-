from django.db import models
from teachers.models import Course

class Attendance(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    course = models.CharField(max_length=30, null=True)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)
        
