from operator import mod
from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name



class Course(models.Model):
    title = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.title






