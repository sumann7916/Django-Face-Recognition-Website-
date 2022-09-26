from django.forms import ModelForm
from students.models import Student
from django import forms

#Create a Student form
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'year', 'semester','course', 'student_img')
         

