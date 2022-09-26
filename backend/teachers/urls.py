from django.urls import path
from .views import login_user, add_students

urlpatterns = [
    path('login_user', login_user, name='login_user'),
    path('add', add_students, name='add_students'),
]
