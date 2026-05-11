from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)  

@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)
    
    serializer = StudentSerializer(student)
    return Response(serializer.data)