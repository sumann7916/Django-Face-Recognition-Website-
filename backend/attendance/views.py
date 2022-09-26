from datetime import date, datetime
import imp
from re import sub
import re
from time import timezone
from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from .forms import AttendanceForm
import face_recognition as fr
import numpy as np
from django.contrib.auth.decorators import login_required
from students.models import Student
from attendance.models import Attendance
from teachers.models import Course


def take_attendance(request):
    submitted = False
    if request.method == "POST":
        form = AttendanceForm(request.POST, request.FILES, teacher=request.user.teacher)
        if form.is_valid():
            course = request.POST['course']
            ipadress = request.POST['IP_address']
            class_img = request.FILES['class_img']
            print("\n\n\n\n\n\n")
            

            #******Recognize Faces from Image******#
            #Load Image
            image = fr.load_image_file(class_img)
            unknown_encodings = fr.face_encodings(image)
            
            #Get all student's face data from that specific course
            encoding_list = []
            studentList =Student.objects.filter(course=course)
            course = Course.objects.filter(id=course)[0].title
            for s in studentList:
                encoding_list.append(s.face_encoding)

            #Compare their faces with class image
            for e in encoding_list:
                #Converting encoding into numpy array
                e= np.array(e)
                result = fr.compare_faces(e, unknown_encodings)
                e= list(e)
                student= Student.objects.filter(face_encoding=e)
                first_name = student[0].first_name
                last_name = student[0].last_name
                print(course)

                if True in result:
                    print("Its a match")
                    #Mark as present in database
                    a = Attendance(first_name = first_name, last_name=last_name,course=course,is_present=True)
                    a.save()
                   
                else:
                    #Mark as Absent in database
                    print("Its not a match")
                    a = Attendance(first_name = first_name, last_name=last_name,course=course,is_present=False)
                    a.save()





    
    form = AttendanceForm(teacher=request.user.teacher)
    context = {
        'form': form,
        }

    return render(request, 'take_attendance.html', context)
    

#View Attendance
def view_attendance(request, course_id):
    if request.method == "POST":
        date = request.POST['date']
    course = Course.objects.filter(id=course_id)[0].title
    #Set Default date to today
    # attendance = Attendance.objects.filter(course=course).filter(date__year = datetime.now().year, date__month = datetime.now().month, date__year = datetime.now().day)
    print("\n\n\n\n\n\n")
    students =Student.objects.filter(course=course_id)
    context = {
        'course': course,
        'students': students
    
    }
    return render(request, 'view_attendance.html', context)

