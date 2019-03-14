from django.urls import path

from . import views

urlpatterns = [
    path('students', views.ListStudent.as_view()),
    path('students/<int:pk>/', views.DetailStudent.as_view()),
    path('courses/', views.ListCourse.as_view()),
    path('courses/<int:pk>/', views.DetailCourse.as_view()),
    path('enrollments/', views.ListEnrollment.as_view()),
    path('enrollments/<int:pk>/', views.DetailEnrollment.as_view()),
]
