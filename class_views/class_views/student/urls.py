from django.urls import path
# from .views import StudentAPI, 
from .views import StudentListApi
urlpatterns = [
    # path('students/', StudentAPI.as_view()),
    # path('students/<int:pk>/', StudentAPI.as_view()),
    path('', StudentListApi.as_view()),
    path('stud/<int:pk>/', StudentListApi.as_view())
]