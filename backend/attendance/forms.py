from dataclasses import field, fields
from django.forms import ModelForm
from students.models import Student
from teachers.models import Course
from django import forms

#Create a Student form
class AttendanceForm(forms.Form):
        course = forms.ModelChoiceField(queryset=Course.objects.all())
        IP_address = forms.GenericIPAddressField()
        class_img = forms.ImageField()

        def __init__(self, *args, **kwargs):
            #using kwargs
            teacher = kwargs.pop('teacher', None)
            super(AttendanceForm, self).__init__(*args, **kwargs)
            self.fields['course'].queryset = Course.objects.filter(teacher=teacher)