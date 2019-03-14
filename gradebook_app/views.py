from rest_framework import generics

from .models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
from django.db.models import OuterRef, Subquery


class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ListCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    # get student objects based on id property
    # Student.objects.filter(id__in=Subquery(Enrollment.objects.filter(course_id=8).values_list('student_id'))).values_list('name')

    # queryset |= Student.objects.filter(id__in=Subquery(Enrollment.objects.filter(course_id=8).values_list('student_id'))).values_list('name')
    serializer_class = CourseSerializer


class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ListEnrollment(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class DetailEnrollment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
