from django.urls import path
from .views import take_attendance, view_attendance

urlpatterns = [
     path('take_attendance', take_attendance, name='take_attendance'),
     path('view/<course_id>', view_attendance, name='view'),
     
 ]
