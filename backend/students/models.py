from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import ArrayField
from teachers.models import Course
from attendance.models import Attendance
from datetime import date, datetime

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    course = models.ManyToManyField(Course)
    student_img = models.ImageField(blank=True,null=True, upload_to="images/")
    face_encoding = ArrayField(base_field=models.FloatField(blank=True, null=True), null=True, blank=True) 

    def __str__(self):
        name = self.first_name + self.last_name
        return name

    def get_encoding(self):
        return self.face_encoding

    def get_attendance(self):
        try:
         return Attendance.objects.filter(first_name=self.first_name)[0].is_present
        except:
            pass
    
    



