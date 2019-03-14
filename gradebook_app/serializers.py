from rest_framework import serializers
from .models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'name',
        )


class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'students',
        )


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            'id',
            'student_id',
            'course_id',
            'grade',
        )
