from re import sub
from django.shortcuts import render
from teachers.models import Course
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def index(request):
    teacher = request.user.teacher
    courses = Course.objects.filter(teacher=request.user.teacher)
    context = {"courses": courses, "teacher": teacher}
    return render(request, 'index.html',  context)
 