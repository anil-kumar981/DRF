from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializer import StudentSerializer

# Create your views here. 
class StudentAPI(APIView):
    # Read All or single data
    # the name of function should be equal to the name of the http methods
    def get(self, request, pk=None):
        if pk is not None:
            try:
                student = Students.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status= status.HTTP_200_OK)
            except:
                return Response({"error":"Student Not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            students = Students.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put (self, request, pk):
        try:
            student = Students.objects.get(id=pk)
        except Students.DoesNotExist:
            return Response({"error":"Student not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            student = Students.objects.get(id=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Students.DoesNotExist:
              return Response({"error":"Student not found"}, status=status.HTTP_400_BAD_REQUEST)