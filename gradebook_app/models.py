from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=128)


class Course(models.Model):
    name = models.CharField(max_length=128)
    students = models.ManyToManyField(Student, through='Enrollment')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3)
