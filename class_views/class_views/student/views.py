from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Students
from .serializer import StudentSerializer

# Create your views here. 
# class StudentAPI(APIView):
#     # Read All or single data
#     # the name of function should be equal to the name of the http methods
#     def get(self, request, pk=None):
#         if pk is not None:
#             try:
#                 student = Students.objects.get(id=pk)
#                 serializer = StudentSerializer(student)
#                 return Response(serializer.data, status= status.HTTP_200_OK)
#             except:
#                 return Response({"error":"Student Not found"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             students = Students.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put (self, request, pk):
#         try:
#             student = Students.objects.get(id=pk)
#         except Students.DoesNotExist:
#             return Response({"error":"Student not found"}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = StudentSerializer(student)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         try:
#             student = Students.objects.get(id=pk)
#             student.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Students.DoesNotExist:
#               return Response({"error":"Student not found"}, status=status.HTTP_400_BAD_REQUEST)
        
# CRUD using generic
class StudentListApi(
    # generic Api view build base class of DRF where query set and serializer are defined
    generics.GenericAPIView,
    # Mixin pre built class where crud operation login is already written   
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    