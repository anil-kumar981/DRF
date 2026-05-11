from django.urls import path
from .views import student_list, student_create, student_detail
urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('students/create/', student_create, name='student-create'),
    path('students/<int:pk>/', student_detail, name='student-detail'),
]