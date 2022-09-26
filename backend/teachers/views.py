import imp
from re import sub
from socket import fromshare
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
import face_recognition as fr

from .forms import StudentForm
from students.models import Student
from .models import Course



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Incorrect username or password"))
            return redirect('login_user')
         
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)

def add_students(request):
    submitted = False
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            #Getting data
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            year = request.POST['year']
            semester = request.POST['semester']
            course = form.cleaned_data.get('course')

            imgObj = request.FILES['student_img']
            image = fr.load_image_file(imgObj)
            encoding = fr.face_encodings(image)[0]
            face_encoding = list(encoding)
            
            s = Student(first_name=first_name, last_name=last_name, year=year, semester=semester, face_encoding=face_encoding)
            s.save()
            for c in course:
                s.course.add(c)

 
            return HttpResponseRedirect('/teachers/add?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
        context = {
            'form': StudentForm,
            'submitted': submitted
        }
        return render(request, 'add_students.html', context)
