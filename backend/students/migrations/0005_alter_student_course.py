# Generated by Django 4.1.1 on 2022-09-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_name'),
        ('students', '0004_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='teachers.course'),
        ),
    ]
