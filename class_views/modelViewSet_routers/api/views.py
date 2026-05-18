from .models import Students
from rest_framework import viewsets
from .serializer import StudentSerializer

# CRUD using viewset
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
